from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
)

from app.db.database import Base


class DocumentPage(Base):

    __tablename__ = "document_pages"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    document_id = Column(
        Integer,
        ForeignKey("documents.id"),
        nullable=False,
    )

    page_number = Column(
        Integer,
        nullable=False,
    )

    text = Column(
        Text,
        nullable=False,
    )