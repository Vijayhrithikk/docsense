from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    Float,
    ForeignKey,
)

from app.db.database import Base


class QuestionLog(Base):

    __tablename__ = "question_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    tenant_id = Column(
        Integer,
        ForeignKey("tenants.id"),
        nullable=False,
    )

    question = Column(
        Text,
        nullable=False,
    )

    answer = Column(
        Text,
        nullable=False,
    )

    retrieval_ms = Column(
        Float,
        nullable=False,
    )

    generation_ms = Column(
        Float,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    top_score = Column(
        Float,
        nullable=True,
    )

    chunk_count = Column(
        Integer,
        nullable=True,
    )

    context_length = Column(
        Integer,
        nullable=True,
    )