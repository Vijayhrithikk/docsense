from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    DateTime
)

from app.db.database import Base
from datetime import datetime


class EvaluationDataset(Base):

    __tablename__ = "evaluation_datasets"

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

    expected_answer = Column(
        Text,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )