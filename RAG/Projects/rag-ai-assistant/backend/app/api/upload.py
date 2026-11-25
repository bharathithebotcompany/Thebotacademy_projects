import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.schema import UploadResponse
from app.rag.loader import load_pdf
from app.rag.chunker import chunk_text
from app.rag.vector_store import create_vector_store
from app.utils.logger import logger

router = APIRouter()

UPLOAD_DIR = "app/data/documents"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload", response_model=UploadResponse)
def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    logger.info(f"File saved at {file_path}")

    text = load_pdf(file_path)

    documents = chunk_text(
        text=text,
        source=file.filename
    )

    create_vector_store(documents)

    return UploadResponse(
        filename=file.filename,
        status=f"Uploaded, chunked & indexed ({len(documents)} chunks)"
    )
