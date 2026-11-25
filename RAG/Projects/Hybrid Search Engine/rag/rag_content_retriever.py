from base.constants import Constants
from rag.rag_corpus_manager import RAGCorpusManager
from typing import List, Tuple

import faiss
import heapq
import numpy as np
import torch


class RAGContentRetriever:
    """
    Handle end-to-end passage retrieval in a Retrieval-Augmented Generation (RAG) system.

    Integrates two main components:
      1. Bi-encoder (FAISS index) for fast passage retrieval.
      2. Cross-encoder for semantic re-ranking of candidate passages.

    Note: Response generation is handled by the agent layer (RagAgent), not this class.

    Usage:
        retriever = RAGContentRetriever(cross_encoder)
    """

    def __init__(self, cross_encoder):
        """
        Initialize the RAGContentRetriever.

        Args:
            cross_encoder: Pretrained cross-encoder model (e.g., from sentence-transformers).
        """
        self._cross_encoder = cross_encoder

    def _merge_passage_chunks_and_scores(self, chunks_list) -> Tuple[str, float]:
        """
        Merge overlapping text chunks and compute their average relevance score.

        Args:
            chunks_list (list[tuple]): List of tuples, each containing:
                - start_word_index (int): Start position of the chunk in the original text.
                - chunk_text (str): Chunk text content.
                - score (float): Relevance score assigned by the cross-encoder.

        Returns:
            tuple:
                str: Merged text string from the chunks.
                float: Average relevance score across the merged chunks.
        """
        merged_text_list = []
        chunk_score = 0
        for i in range(len(chunks_list)):
            if (
                i < len(chunks_list) - 1
                and chunks_list[i + 1][0] <= chunks_list[i][0] + len(chunks_list[i][1]) - 1
            ):
                merged_text_list.append(
                    chunks_list[i][1][: chunks_list[i + 1][0] - chunks_list[i][0]]
                )
            else:
                merged_text_list.append(chunks_list[i][1])
            chunk_score += chunks_list[i][2]
        return " ".join(merged_text_list), chunk_score / len(chunks_list)

    def _biencoder_find_top_similar_items(
        self, query: str, top_k: int, rag_corpus: RAGCorpusManager
    ) -> Tuple[List[int], List[float]]:
        """
        Retrieve top-k semantically similar passages using the FAISS bi-encoder index.

        Args:
            query (str): Query text to search for.
            top_k (int): Number of top results to retrieve.
            rag_corpus (RAGCorpusManager): Corpus manager containing FAISS index and embeddings.

        Returns:
            tuple[list[int], list[float]]: Indices and corresponding similarity scores of the top-k chunks.
        """
        query_embedding = rag_corpus.sentence_transformer.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(query_embedding)
        scores, indices = rag_corpus.faiss_index.search(query_embedding, top_k)
        return indices[0].tolist(), scores[0].tolist()

    @staticmethod
    def _minmax_normalize(scores: np.ndarray) -> np.ndarray:
        """Min-max normalise a score array to the [0, 1] range.

        Args:
            scores (np.ndarray): Raw score values to normalise.

        Returns:
            np.ndarray: Normalised scores in [0, 1].
        """
        min_s, max_s = scores.min(), scores.max()
        if max_s - min_s < 1e-9:
            return np.ones_like(scores)
        return (scores - min_s) / (max_s - min_s + 1e-9)

    def _hybrid_score_and_rank(
        self,
        biencoder_indices: List[int],
        biencoder_scores: np.ndarray,
        bm25_indices: List[int],
        bm25_scores: np.ndarray,
        semantic_weight: float,
        lexical_weight: float,
        top_k: int,
    ) -> List[int]:
        """
        Combine bi-encoder and BM25 scores via a weighted linear sum and return top-k indices.

        Both score vectors are min-max normalised to [0, 1] before combining so that
        their different scales do not bias the result.

        Args:
            biencoder_indices (list[int]): Chunk indices returned by the bi-encoder.
            biencoder_scores (np.ndarray): Corresponding bi-encoder similarity scores.
            bm25_indices (list[int]): Chunk indices returned by BM25.
            bm25_scores (np.ndarray): Corresponding BM25 scores.
            semantic_weight (float): Weight applied to the normalised bi-encoder score.
            lexical_weight (float): Weight applied to the normalised BM25 score.
            top_k (int): Number of top-ranked indices to return.

        Returns:
            list[int]: Indices of the top-k chunks ranked by hybrid score.
        """
        norm_biencoder_scores = self._minmax_normalize(np.array(biencoder_scores, dtype=float))
        norm_bm25_scores = self._minmax_normalize(np.array(bm25_scores, dtype=float))
        hybrid_scores = {}
        for idx, semantic_score in zip(biencoder_indices, norm_biencoder_scores):
            hybrid_scores[idx] = hybrid_scores.get(idx, 0.0) + semantic_weight * float(
                semantic_score
            )
        for idx, lexical_score in zip(bm25_indices, norm_bm25_scores):
            hybrid_scores[idx] = hybrid_scores.get(idx, 0.0) + lexical_weight * float(lexical_score)

        top_k_indices = heapq.nlargest(top_k, hybrid_scores, key=hybrid_scores.__getitem__)
        return top_k_indices

    def _cross_encoder_find_top_similar_items(
        self,
        query: str,
        rag_corpus: RAGCorpusManager,
        passage_chunk_indices: List[int],
        top_k: int = 5,
        batch_size: int = 64,
    ) -> Tuple[List[int], List[float]]:
        """
        Re-rank retrieved passages using a cross-encoder for more precise semantic relevance.

        Args:
            query (str): Input query text.
            rag_corpus (RAGCorpusManager): Corpus manager containing chunked data and metadata.
            passage_chunk_indices (list[int]): Indices of passage chunks retrieved by the bi-encoder.
            top_k (int, optional): Number of top passages to keep after re-ranking. Defaults to 5.
            batch_size (int, optional): Number of passage pairs to process in a single batch. Defaults to 64.

        Returns:
            tuple[list[int], list[float]]: Indices and corresponding cross-encoder scores of the
            top-k chunks, sorted by descending relevance.
        """
        self._cross_encoder.eval()
        scores = []

        with torch.no_grad():
            for start in range(0, len(passage_chunk_indices), batch_size):
                batch_indices = passage_chunk_indices[start : start + batch_size]
                batch_passages = [rag_corpus.chunked_data[i] for i in batch_indices]
                batch_pairs = [[query, passage] for passage in batch_passages]
                batch_scores = self._cross_encoder.predict(batch_pairs)
                scores.extend(zip(batch_indices, batch_scores))
        most_related_items_index_score_pairs = sorted(scores, key=lambda x: x[1], reverse=True)[
            :top_k
        ]
        top_indices = [idx for idx, _ in most_related_items_index_score_pairs]
        top_scores = [float(score) for _, score in most_related_items_index_score_pairs]
        return top_indices, top_scores

    def find_top_similar_items(
        self,
        rag_corpus: RAGCorpusManager,
        query: str,
        initial_retrieval_top_k: int = 100,
        cross_encoder_top_k: int = 5,
        cross_encoder_batch_size: int = 16,
        semantic_similarity_weight: float = 1.0,
        lexical_similarity_weight: float = 0.0,
    ) -> Tuple[List[int], List[float]]:
        """
        Retrieve top similar passages to the query using hybrid retrieval.

        Scores from the bi-encoder (semantic) and BM25 (lexical) are each min-max
        normalised then combined as a weighted linear sum. The resulting top-k
        candidates are re-ranked by the cross-encoder.

        Args:
            rag_corpus (RAGCorpusManager): Corpus manager containing documents, embeddings, and metadata.
            query (str): User query string.
            initial_retrieval_top_k (int, optional): Number of passages retrieved by each of the bi-encoder and BM25. Defaults to 100.
            cross_encoder_top_k (int, optional): Number of passages kept after cross-encoder re-ranking. Defaults to 5.
            cross_encoder_batch_size (int, optional): Batch size for cross-encoder inference. Defaults to 16.
            semantic_similarity_weight (float, optional): Weight for semantic (bi-encoder) score. Defaults to 0.8.
            lexical_similarity_weight (float, optional): Weight for lexical (BM25) score. Defaults to 0.2.

        Returns:
            tuple[list[int], list[float]]: Indices and corresponding cross-encoder scores of the
            top-k chunks, sorted by descending relevance.
        """
        if rag_corpus.faiss_index.ntotal == 0:
            return [], []
        biencoder_indices, biencoder_scores = self._biencoder_find_top_similar_items(
            query, initial_retrieval_top_k, rag_corpus
        )
        if lexical_similarity_weight != 0.0:
            bm25_indices, bm25_scores = rag_corpus.bm25_retriever.search(
                query, top_k=initial_retrieval_top_k
            )
            hybrid_top_indices = self._hybrid_score_and_rank(
                biencoder_indices,
                biencoder_scores,
                bm25_indices,
                bm25_scores,
                semantic_similarity_weight,
                lexical_similarity_weight,
                initial_retrieval_top_k,
            )
        else:
            hybrid_top_indices = biencoder_indices
        cross_encoder_top_indices, cross_encoder_top_scores = (
            self._cross_encoder_find_top_similar_items(
                query,
                rag_corpus,
                hybrid_top_indices,
                cross_encoder_top_k,
                cross_encoder_batch_size,
            )
        )
        return cross_encoder_top_indices, cross_encoder_top_scores
