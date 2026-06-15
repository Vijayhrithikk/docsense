from sqlalchemy import (
    String,
    Integer,
    Column,
    ForeignKey,
    Text,
    DateTime,
    JSON
)

from datetime import datetime

from sqlalchemy.orm import relationship

from app.db.database import Base

class ChunkEmbedding(Base):

    __tablename__ = "chunk_embeddings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    chunk_id = Column(
        Integer,
        ForeignKey("chunks.id"),
        nullable=False,
    )

    model_name = Column(
        Text,
        nullable=False
    )

    embedding = Column(
        JSON,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    