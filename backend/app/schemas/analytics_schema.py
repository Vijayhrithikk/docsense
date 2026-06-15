from pydantic import BaseModel


class AnalyticsResponse(
    BaseModel
):

    total_questions: int

    avg_retrieval_ms: float

    avg_generation_ms: float

    avg_top_score: float

    avg_chunk_count: float

    avg_context_length: float

