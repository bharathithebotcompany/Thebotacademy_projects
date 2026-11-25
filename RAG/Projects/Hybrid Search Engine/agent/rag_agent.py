from rag.rag_content_retriever import RAGContentRetriever
from rag.rag_corpus_manager import RAGCorpusManager
from base.constants import Constants

import datetime
import json
import os
import re


class RagAgent:
    # For query engineering, start with just rewriting query -> then implement decomposition

    def __init__(self, corpus_manager: RAGCorpusManager, rag_retriever: RAGContentRetriever):
        self.history_corpus = corpus_manager
        self.rag_retriever = rag_retriever
        self.logs_dir = "./logs/"
        self.logs_file_name = (
            f"rag_agent_logs_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

    def _save_responses_and_context_to_json_logs(self, **kwargs):
        """Saves the query, response, and context to a JSON log file with a timestamped filename.

        The log entry includes the original query, the generated response, the retrieved context passages, and a timestamp of when the interaction occurred.

        Args:
            **kwargs: Arbitrary keyword arguments representing the log entry fields.
        """

        log_entry = {"timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), **kwargs}
        os.makedirs(self.logs_dir, exist_ok=True)
        log_file_path = os.path.join(self.logs_dir, self.logs_file_name)
        if os.path.exists(log_file_path):
            with open(log_file_path, "r") as log_file:
                existing_logs = json.load(log_file)
        else:
            existing_logs = []
        existing_logs.append(log_entry)
        with open(log_file_path, "w") as log_file:
            json.dump(existing_logs, log_file, indent=4)

    def improve_query(
        self,
        query: str,
        generative_model,
        **kwargs,
    ) -> str:
        """Rewrites the user query to be clearer and better suited for retrieval.

        Uses Constants.Instructions.RAGAgent.QUERY_REWRITER as the system instructions

        Args:
            query (str): The original user query.
            generative_model: Callable that accepts prompt and system_instructions parameters and returns a string.
            **kwargs: Extra keyword arguments forwarded to the generative model (e.g. config).

        Returns:
            str: The rewritten query.
        """
        prompt = f"Query: {query}"
        improved_query = generative_model(
            prompt,
            system_instructions=Constants.Instructions.RAGAgent.QUERY_REWRITER,
            **kwargs,
        )
        return improved_query

    def summarize_context(
        self,
        query: str,
        context: str,
        generative_model,
        **kwargs,
    ) -> str:
        """Produces a concise, query-focused summary of the retrieved context passages.

        Uses Constants.Instructions.RAGAgent.CONTEXT_SUMMARIZER as the system instruction.

        Args:
            query (str): The user query that guides the summarization focus.
            context (str): Retrieved context passage to summarize.
            generative_model: Callable that accepts prompt and system_instructions parameters and returns a string.
            **kwargs: Extra keyword arguments forwarded to the generative model (e.g. config).

        Returns:
            str: A brief summary of the relevant context.
        """
        prompt = f"Query: {query}\nContext:\n{context}"
        return generative_model(
            prompt,
            system_instructions=Constants.Instructions.RAGAgent.CONTEXT_SUMMARIZER,
            **kwargs,
        )

    @staticmethod
    def _parse_json_response(raw: str) -> dict:
        """Extracts and parses the first JSON object found in the LLM response.

        Args:
            raw (str): Raw LLM output, optionally wrapped in markdown fences or containing extra text.

        Returns:
            dict: Parsed JSON object, or the original string if no valid JSON is found.
        """
        if isinstance(raw, dict):
            return raw
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
        return raw

    def check_citation_correctness(
        self, query: str, response: str, context: str, generative_model, **kwargs
    ) -> dict:
        """Checks the correctness of the citations in the generated response based on the retrieved context.

        Uses Constants.Instructions.RAGAgent.CITATION_CHECKER as the system instruction.

        Args:
            query (str): The original user query.
            response (str): The generated response that may contain citations.
            context (str): The retrieved context passages that should support the response.
            generative_model: Callable that accepts prompt and system_instructions parameters and returns a string.
            **kwargs: Extra keyword arguments forwarded to the generative model (e.g. config).

        Returns:
            dict: Parsed citation verification result with keys "verified", "unsupported", and "verdict".
        """
        prompt = f"Query: {query}\n\nResponse:\n{response}\n\nContext:\n{context}\n\nEvaluate the correctness of the citations in the response based on the context."
        citation_check_response = generative_model(
            prompt,
            system_instructions=Constants.Instructions.RAGAgent.CITATION_CHECKER,
            **kwargs,
        )
        return self._parse_json_response(citation_check_response)

    def retrieve_relevant_context_from_corpus(
        self,
        query: str,
        corpus: RAGCorpusManager,
        **rag_retriever_kwargs,
    ):
        """Retrieves relevant context for a given query using the specified RAG retriever and corpus.

        Args:
            query (str): The input query for which to retrieve relevant context.
            corpus (RAGCorpusManager): The RAG corpus manager containing the indexed data to search.
            **rag_retriever_kwargs: Additional keyword arguments to pass to the retriever (e.g., retrieval parameters).

        Returns:
            tuple[list[str], list[dict]]: A tuple containing a list of retrieved context strings and a corresponding list of their metadata dictionaries.
        """
        indices, scores = self.rag_retriever.find_top_similar_items(
            rag_corpus=corpus, query=query, **rag_retriever_kwargs
        )
        positive_mask = [score > 0 for score in scores]
        indices = [index for index, keep in zip(indices, positive_mask) if keep]
        scores = [score for score, keep in zip(scores, positive_mask) if keep]
        if not indices:
            return [], []
        retrieved_context = [(corpus.chunked_data[idx]) for idx in indices]
        retrieved_context_metadata = [corpus.chunked_data_metadata[idx] for idx in indices]
        return retrieved_context, retrieved_context_metadata

    def _add_query_and_response_to_history_corpus(self, query: str, metadata: dict):
        """Adds the user query and the corresponding model response to the agent's history corpus for future retrieval and reference.

        Note: The queries are stored as main context for retrieval (search in history corpus is done based on the queries)
        Note: Responses are stored in the metadata of the history corpus.

        Args:
            query (str): The user query to add to the history corpus.
            metadata (dict): Metadata dictionary containing response details and other information.

        Returns:
            None
        """
        self.history_corpus.add_update_data_and_index(texts=[query], metadatas=[metadata])

    def _summarize_and_build_contexts_string(
        self,
        query: str,
        retrieved_context: list,
        generative_model,
        summarize_context_kwargs_dict: dict | None = None,
    ) -> tuple[list, str]:
        """Summarizes each retrieved passage and formats them into a numbered context string.

        Args:
            query (str): The user query, used to focus each summary.
            retrieved_context (list[str]): Raw retrieved passages.
            generative_model: Callable that accepts prompt and system_instructions parameters and returns a string.
            summarize_context_kwargs_dict (dict | None): Extra keyword arguments forwarded to the
                generative model inside summarize_context (e.g. config). Defaults to None.

        Returns:
            tuple[list[str], str]: The summarized passages and the formatted context string.
        """
        if not retrieved_context:
            return [], "Context: "
        summarized_context = [
            self.summarize_context(
                query,
                passage,
                generative_model,
                **(summarize_context_kwargs_dict or {}),
            )
            for passage in retrieved_context
        ]
        summarized_contexts_string = "\n\n".join(
            f"Context {i + 1}: {passage}" for i, passage in enumerate(summarized_context)
        )
        return summarized_context, summarized_contexts_string

    def _generate_response_from_context(
        self,
        query: str,
        contexts_string: str,
        generative_model,
        **generative_model_kwargs,
    ) -> str:
        """Builds the prompt and calls the generative model to produce a grounded response.

        Args:
            query (str): The user query.
            contexts_string (str): Formatted numbered context string.
            generative_model: Callable that accepts prompt and system_instructions parameters and returns a string.
            **generative_model_kwargs: Extra keyword arguments forwarded to the generative model
                (e.g. config=my_config to override the default generation config).

        Returns:
            str: The raw model response.
        """
        prompt = f"Query: {query}\n{contexts_string}"
        return generative_model(
            prompt,
            system_instructions=Constants.Instructions.RAGAgent.RESPONSE_GENERATOR,
            **generative_model_kwargs,
        )

    def get_query_response(
        self,
        *,
        query: str,
        rag_corpus: RAGCorpusManager,
        similarity_score_threshold: float,
        semantic_similarity_weight: float,
        lexical_similarity_weight: float,
        cross_encoder_top_k: int,
        generative_model,
        use_agent_history: bool = True,
        rag_retriever_kwargs_dict: dict | None = None,
        improve_query_kwargs_dict: dict | None = None,
        summarize_context_kwargs_dict: dict | None = None,
        generate_response_kwargs_dict: dict | None = None,
        citation_check_kwargs_dict: dict | None = None,
    ) -> dict:
        """Generates a grounded answer for the query using retrieved context or agent history.

        First rewrites the query, then checks agent history for a sufficiently similar past
        response. If a match is found, returns it directly. Otherwise, retrieves and summarizes
        fresh context from the RAG corpus, generates a response, performs citation checking, and
        stores the result in both history and logs.

        The returned dict always contains these keys:
            - query (str): Original user query.
            - improved_query (str): Rewritten query used for retrieval.
            - response_type (str): "agent_history" | "generative_model".
            - response (str): The answer text.
            - context (list[str]): Summarized context passages used to produce the response.
            - citation_check_response (dict): Citation verification result from the LLM.
            - agent_history_metadata (dict | None): Present on both paths.
                On "agent_history": {"relevance_score": float, "history_query": str}.
                On "generative_model": None.

        Args:
            query (str): The user query.
            rag_corpus (RAGCorpusManager): The knowledge-base corpus to retrieve from.
            similarity_score_threshold (float): Minimum similarity score to consider an agent history hit valid.
            semantic_similarity_weight (float): Weight for dense/semantic retrieval.
            lexical_similarity_weight (float): Weight for sparse/lexical retrieval.
            cross_encoder_top_k (int): Number of passages to keep after cross-encoder re-ranking.
            generative_model: Callable that accepts prompt and system_instructions parameters and returns a string.
            use_agent_history (bool): Whether to check the agent history before doing a fresh
                retrieval. Defaults to True.
            rag_retriever_kwargs_dict (dict | None): Extra keyword arguments forwarded to
                retrieve_relevant_context_from_corpus. Defaults to None (no extras).
            improve_query_kwargs_dict (dict | None): Extra keyword arguments forwarded to the
                generative model inside improve_query (e.g. a faster/cheaper config).
                Defaults to None (no extras).
            summarize_context_kwargs_dict (dict | None): Extra keyword arguments forwarded to the
                generative model inside summarize_context. Defaults to None (no extras).
            generate_response_kwargs_dict (dict | None): Extra keyword arguments forwarded to the
                generative model inside _generate_response_from_context. Defaults to None (no extras).
            citation_check_kwargs_dict (dict | None): Extra keyword arguments forwarded to the
                generative model inside check_citation_correctness. Defaults to None (no extras).

        Returns:
            dict: Response details with the keys described above.
        """
        improved_query = self.improve_query(
            query,
            generative_model,
            **(improve_query_kwargs_dict or {}),
        )

        # --- 1. History lookup ---
        if use_agent_history:
            history_hit = self._check_agent_history_for_relevant_info(
                improved_query, similarity_threshold=similarity_score_threshold
            )
            if history_hit is not None:
                response_details_dict = {
                    "query": query,
                    "improved_query": improved_query,
                    "response_type": "agent_history",
                    "agent_history_metadata": {
                        "relevance_score": history_hit["relevance_score"],
                        "history_query": history_hit["history_query"],
                    },
                    "response": history_hit["response"],
                    "context": history_hit["context"],
                    "citation_check_response": history_hit["citation_check_response"],
                }
                self._save_responses_and_context_to_json_logs(**response_details_dict)
                return response_details_dict

        # --- 2. Fresh retrieval ---
        retrieved_context, _ = self.retrieve_relevant_context_from_corpus(
            improved_query,
            rag_corpus,
            cross_encoder_top_k=cross_encoder_top_k,
            semantic_similarity_weight=semantic_similarity_weight,
            lexical_similarity_weight=lexical_similarity_weight,
            **(rag_retriever_kwargs_dict or {}),
        )

        # --- 3. Summarize context and generate response ---
        summarized_context, contexts_string = self._summarize_and_build_contexts_string(
            query=improved_query,
            retrieved_context=retrieved_context,
            generative_model=generative_model,
            summarize_context_kwargs_dict=(summarize_context_kwargs_dict or {}),
        )
        response = self._generate_response_from_context(
            query,
            contexts_string,
            generative_model,
            **(generate_response_kwargs_dict or {}),
        )

        # --- 4. Citation check ---
        citation_check_response = self.check_citation_correctness(
            improved_query,
            response,
            contexts_string,
            generative_model,
            **(citation_check_kwargs_dict or {}),
        )

        # --- 5. Persist and return ---
        response_details_dict = {
            "query": query,
            "improved_query": improved_query,
            "response_type": "generative_model",
            "agent_history_metadata": None,
            "response": response,
            "context": summarized_context,
            "citation_check_response": citation_check_response,
        }
        self._add_query_and_response_to_history_corpus(improved_query, response_details_dict)
        self._save_responses_and_context_to_json_logs(**response_details_dict)
        return response_details_dict

    def _check_agent_history_for_relevant_info(
        self,
        query: str,
        similarity_threshold: float,
    ):
        """Check the agent's history corpus for relevant information based on the query.

        Returns the response from the most similar item in the history if its similarity score meets or exceeds the threshold; otherwise, returns None.

        Args:
            query (str): The input query to check against the history.
            similarity_threshold (float): The minimum similarity score required to consider a match relevant.

        Returns:
            dict or None: A dictionary containing relevance_score, history_query, response, context, and citation_check_response if a match is found; otherwise, None.
        """
        indices, scores = self.rag_retriever.find_top_similar_items(
            rag_corpus=self.history_corpus,
            query=query,
            cross_encoder_top_k=1,
        )
        if scores and scores[0] >= similarity_threshold:
            meta = self.history_corpus.chunked_data_metadata[indices[0]]
            return {
                "relevance_score": scores[0],
                "history_query": meta["query"],
                "response": meta["response"],
                "context": meta["context"],
                "citation_check_response": meta["citation_check_response"],
            }
        else:
            return None
