from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel


class AskQuestionRequest(BaseModel):

    tenant_id: int

    question: str


class SourceResponse(BaseModel):

    document_title: str

    start_page: int

    end_page: int

    score: float


class AskQuestionResponse(BaseModel):

    answer: str

    sources: list[SourceResponse]

class QuestionHistoryItem(BaseModel):

    id: int

    question: str

    answer: str

    retrieval_ms: float

    generation_ms: float

    created_at: datetime

    class Config:

        from_attributes = True