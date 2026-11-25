from agent.rag_agent import RagAgent
from base.constants import Constants
from config import HF_TOKEN, GOOGLE_API_KEY
from google.genai import types
from rag.rag_content_retriever import RAGContentRetriever, RAGCorpusManager
from utils.dataset_utils import DataSetUtil
from utils.model_loader import ModelLoader

if __name__ == "__main__":
    # ============================================================================
    # STEP 1: Load Models and Components
    # ============================================================================

    # Initialize the model loader utility to load various AI models
    model_loader = ModelLoader()

    # Load cross-encoder model for re-ranking retrieved documents
    cross_encoder = model_loader.load_hf_cross_encoder(hugging_face_token=HF_TOKEN)

    # Load sentence transformer model for generating text embeddings
    sentence_transformer = model_loader.load_sentence_embedding_model(hugging_face_token=HF_TOKEN)

    generative_model_config = types.GenerateContentConfig(
        temperature=0.5,
        system_instruction=None,
    )
    generative_model = model_loader.load_gemini_generative_model(
        google_api_key=GOOGLE_API_KEY,
        config=generative_model_config,
        model_name=Constants.ModelNames.Gemini.GEMINI_2_5_FLASH,
    )

    # ============================================================================
    # STEP 2: Initialize RAG Components
    # ============================================================================

    # Create a RAG corpus manager for the knowledge base (local documents)
    rag_corpus_manager_for_knowledge_base = RAGCorpusManager(
        sentence_transformer=sentence_transformer
    )

    # Create a separate RAG corpus manager for web search results
    rag_corpus_manager_for_rag_agent_history = RAGCorpusManager(
        sentence_transformer=sentence_transformer
    )

    # Load the knowledge base dataset (SQuAD dataset)
    dataset_util = DataSetUtil()
    knowledge_base = dataset_util.load_qa_dataset(samples_count=10000)

    # Index the knowledge base documents into the corpus manager
    rag_corpus_manager_for_knowledge_base.add_update_data_and_index(
        texts=[item["context"] for item in knowledge_base],
        metadatas=[{k: v for k, v in item.items() if k != "context"} for item in knowledge_base],
    )

    # Initialize the content retriever with cross-encoder for re-ranking
    rag_content_retriever = RAGContentRetriever(cross_encoder)

    # ============================================================================
    # STEP 3: Initialize RAG agent and Run example queries
    # ============================================================================

    # Initialize the RAG agent with both corpus managers and the content retriever
    rag_agent = RagAgent(rag_corpus_manager_for_rag_agent_history, rag_content_retriever)

    # Run example queries through the RAG agent and print responses with context
    for query in [
        "Which NFL team won Super Bowl 50?",
        "Which NFL team won Super Bowl 50?",
        "Which university did Nikola Tesla attend?",
        "What is in front of the Notre Dame Main Building?",
        "When did the Scholastic Magazine of Notre Dame begin publishing?",
        "What is the daily student paper at Notre Dame called?",
        "What is the name of the author Chopin met at a gathering put on by Marie d'Agoult?",
        "How many days did people have to wait to marry after a divorce?",
        "What is in front of the Notre Dame Main Building?",
        "Who published a Seismic Risk Analysis Study?",
        "What is the capital of Australia?",
        "Who wrote Harry Potter novels?",
    ]:
        result = rag_agent.get_query_response(
            query=query,
            rag_corpus=rag_corpus_manager_for_knowledge_base,
            similarity_score_threshold=6.5,
            generative_model=generative_model,
            semantic_similarity_weight=0.8,
            lexical_similarity_weight=0.2,
            cross_encoder_top_k=3,
        )
        context_refs = "\n".join(
            [
                f"[{i+1}] {text[:100]}..."  # Show only the first 100 characters of each context passage
                for i, text in enumerate(result.get("context", []))
            ]
        )
        print(
            f"\n\n<<<<<<<<<<<<<<<<<<<{query}>>>>>>>>>>>>>>>>>\nresponse type: {result.get('response_type')}\nresponse: {result['response']}\n{context_refs}"
        )
