from app.models.document_page_model import DocumentPage

from sqlalchemy.orm import Session

def create_document_page(
        db: Session,
        document_id: int,
        page_number: int,
        text: str
):
    page = DocumentPage(document_id=document_id, page_number=page_number, text=text)
    db.add(DocumentPage)
    
    return page

def create_document_pages(db: Session, pages: list[DocumentPage]):

    db.add_all(pages)
    db.commit()

    return pages


def bulk_create_pages(db: Session, document_id : int, pages: list[dict]):

    records = [
        DocumentPage(
            document_id=document_id,
            page_number=page["page"],
            text=page["text"],
        )
        for page in pages
    ]

    db.add_all(records)

    db.commit()

    return records