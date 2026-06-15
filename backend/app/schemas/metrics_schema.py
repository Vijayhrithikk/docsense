from pydantic import BaseModel


class MetricsResponse(BaseModel):

    documents: int

    chunks: int

    questions: int

    evaluations: int