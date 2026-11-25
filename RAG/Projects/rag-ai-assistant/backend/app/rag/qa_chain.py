from transformers import pipeline
from fastapi import HTTPException
from app.utils.logger import logger
from app.rag.vector_store import load_vector_store


# Load LLM once (important for performance)
def load_llm():
    logger.info("Loading HuggingFace LLM (flan-t5-base)")

    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_length=512
    )


llm = load_llm()


def answer_question(question: str) -> str:
    logger.info(f"Answering question: {question}")

    # 1️⃣ Load vector store safely
    try:
        vector_store = load_vector_store()
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="No documents uploaded yet"
        )

    # 2️⃣ Retrieve relevant documents
    docs = vector_store.similarity_search(question, k=4)

    if not docs:
        logger.warning("No relevant documents found")
        return "I don't know. The document does not contain this information."

    # 3️⃣ Build context safely
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Answer the question using ONLY the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
""".strip()

    # 4️⃣ Call LLM
    result = llm(prompt)

    if not result or "generated_text" not in result[0]:
        logger.error("LLM returned empty response")
        return "I couldn't generate an answer."

    answer = result[0]["generated_text"].strip()

    if not answer:
        logger.error("Generated answer is empty")
        return "I couldn't find an answer in the document."

    logger.info("Answer generated successfully")
    return answer
