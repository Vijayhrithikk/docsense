from app.db.session import SessionLocal
import app.models

from app.services.question_answer_service import (
    QuestionAnswerService,
)

db = SessionLocal()

service = QuestionAnswerService()

response = service.retrieval_service.retrieve(
    db,
    1,
    "what is a skill",
    top_k=5
)

print(response)

db.close()