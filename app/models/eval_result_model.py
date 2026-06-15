from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Float,
    Boolean,
    DateTime,
)

from app.db.database import Base


class EvaluationResult(Base):

    __tablename__ = "evaluation_results"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    total_cases = Column(
        Integer,
        nullable=False,
    )

    passed_cases = Column(
        Integer,
        nullable=False,
    )

    recall_at_3 = Column(
        Float,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    answer_relevancy = Column(
        Float,
        nullable=True 
    )

    faithfulness = Column(
        Float,
        nullable=True
    )