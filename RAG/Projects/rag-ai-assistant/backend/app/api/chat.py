import os
from fastapi import APIRouter, HTTPException
from app.models.schema import ChatRequest, ChatResponse
from app.rag.qa_chain import answer_question
from app.db.database import SessionLocal
from app.db.models import ChatHistory
from app.utils.logger import logger

router = APIRouter()

VECTOR_DB_PATH = "app/data/vector_store"


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # ✅ Guard 1: empty question
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    # ✅ Guard 2: vector store must exist
    if not os.path.exists(VECTOR_DB_PATH):
        return ChatResponse(
            answer="Please upload a document before asking questions."
        )

    try:
        answer = answer_question(request.question)

        # ✅ Guard 3: answer must not be empty
        if not answer:
            raise ValueError("Empty answer generated")

    except Exception as e:
        logger.error(f"Chat processing failed: {e}")
        answer = (
            "I could not generate an answer. "
            "Please try another question or upload a different document."
        )

    # ✅ SAFE DB INSERT (answer is ALWAYS non-null now)
    db = SessionLocal()
    try:
        chat_entry = ChatHistory(
            question=request.question,
            answer=answer
        )
        db.add(chat_entry)
        db.commit()
    finally:
        db.close()

    logger.info("Chat saved to database")

    return ChatResponse(answer=answer)

