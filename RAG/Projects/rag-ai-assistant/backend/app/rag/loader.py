from langchain_community.document_loaders import PyPDFLoader

from app.utils.logger import logger

def load_pdf(file_path: str) -> str:
    """
    Load PDF file and extract text
    """
    logger.info(f"Loading PDF from {file_path}")

    loader = PyPDFLoader(file_path)
    pages = loader.load()

    text = ""
    for page in pages:
        text += page.page_content + "\n"

    return text
