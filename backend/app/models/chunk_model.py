from sqlalchemy import (
    String,
    Integer,
    Column,
    ForeignKey,
    Text
)

from sqlalchemy.orm import relationship

from app.db.database import Base

class Chunk(Base):

    __tablename__ = "chunks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    document_id = Column(
        Integer,
        ForeignKey("documents.id"),
        nullable=False,
    )

    start_page = Column(
        Integer,
        nullable=False
    )

    end_page = Column(
        Integer,
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    document = relationship(
        "Document",
        back_populates="chunks",
    )

    