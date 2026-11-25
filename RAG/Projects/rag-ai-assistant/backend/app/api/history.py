from fastapi import APIRouter
from app.db.database import SessionLocal
from app.db.models import ChatHistory

router = APIRouter()

@router.get("/history")
def get_chat_history():
    db = SessionLocal()
    chats = db.query(ChatHistory).order_by(ChatHistory.created_at.desc()).all()
    db.close()

    return chats
