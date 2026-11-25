from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.utils.logger import logger

def chunk_text(
    text: str,
    source: str,
    chunk_size: int = 800,
    chunk_overlap: int = 200
):
    """
    Split text into overlapping chunks with metadata
    """

    logger.info("Starting text chunking")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_text(text)

    documents = []
    for i, chunk in enumerate(chunks):
        documents.append(
            Document(
                page_content=chunk,
                metadata={
                    "source": source,
                    "chunk_id": i
                }
            )
        )

    logger.info(f"Created {len(documents)} chunks")

    return documents
