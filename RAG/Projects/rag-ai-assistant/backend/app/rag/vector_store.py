import os
from langchain_community.vectorstores import FAISS
from app.rag.embeddings import get_embeddings_model
from app.utils.logger import logger

VECTOR_DB_PATH = "app/data/vector_store"


def create_vector_store(documents):
    logger.info("Creating FAISS vector store")

    # ✅ GUARD: no documents → no FAISS
    if not documents:
        logger.error("No documents provided for vector store creation")
        raise ValueError("No text chunks found. Vector store not created.")

    embeddings = get_embeddings_model()

    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    vector_store.save_local(VECTOR_DB_PATH)

    logger.info("Vector store saved to disk")

    return vector_store


def load_vector_store():
    embeddings = get_embeddings_model()

    if not os.path.exists(VECTOR_DB_PATH):
        logger.error("Vector store not found on disk")
        raise FileNotFoundError("Vector store not found. Please upload a document first.")

    logger.info("Loading FAISS vector store from disk")

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
