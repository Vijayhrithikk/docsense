from sqlalchemy.orm import Session

from app.models.document_model import Document

def create_document(db: Session, tenant_id: int, title: str, filepath: str) -> Document:

    document = Document(
        tenant_id=tenant_id,
        title=title,
        file_path=filepath
    )

    db.add(document)

    db.commit()

    db.refresh(document)

    return document

def get_document(db: Session, document_id: int):

    return db.query(Document).filter(Document.id==document_id).first()

def update_document_status(db: Session, document_id: int, status: str):

    db.query(Document).filter(Document.id==document_id).update({"status":status})

    db.commit()

def update_document_error(db: Session, document_id : int, error_message: str):

    db.query(Document).filter(Document.id==document_id).update({"error_message": error_message})
    db.commit()