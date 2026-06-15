from datetime import datetime

from pydantic import BaseModel


class EvaluationCaseCreate(
    BaseModel
):

    tenant_id: int

    question: str

    expected_answer: str


class EvaluationCaseResponse(
    BaseModel
):

    id: int

    tenant_id: int

    question: str

    expected_answer: str

    created_at: datetime

    class Config:

        from_attributes = True

class EvaluationCaseResult(
    BaseModel):

    question: str

    expected_answer: str

    passed: bool

    top_chunk: str |None=None


class EvaluationRunResponse(
    BaseModel
):

    total_cases: int

    passed_cases: int

    recall_at_3: float

    relevancy: float

    faithfulness: float

    results: list[EvaluationCaseResult]


from datetime import datetime


class EvaluationResultResponse(BaseModel):

    id: int

    total_cases: int

    passed_cases: int

    recall_at_3: float

    created_at: datetime

    answer_relevancy: float | None

    faithfulness: float | None

    class Config:

        from_attributes = True


