from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from app.db.database import Base

class Tenant(Base):

    __tablename__ = "tenants"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False 
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )