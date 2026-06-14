from app.db.session import SessionLocal

from app.services.question_answer_service import (
    QuestionAnswerService,
)

db = SessionLocal()

service = QuestionAnswerService()

response = service.answer(
    db,
    "How claude skill works",
)

print(response)

db.close()