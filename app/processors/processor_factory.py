from app.processors.pdf_processor import (
    PDFProcessor,
)


def get_processor(file_path: str,):

    if file_path.endswith(".pdf"):
        return PDFProcessor()

    raise ValueError("Unsupported file type")