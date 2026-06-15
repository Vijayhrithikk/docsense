from app.db.session import SessionLocal
from fastapi import APIRouter
from app.db.session import get_db
from fastapi import Depends

from app.services.question_answer_service import (
    QuestionAnswerService,
)

db = SessionLocal()
from sqlalchemy.orm import Session

service = QuestionAnswerService()

router = APIRouter()

@router.get("/test")
def run(db: Session = Depends(get_db)):

    response = service.answer(
        db,
        tenant_id=1,

        question="How claude skill works",
    )

    return response