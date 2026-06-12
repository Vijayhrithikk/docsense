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