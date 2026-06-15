from app.repositories.analytics_repo import (
    get_analytics,
)


class AnalyticsService:

    def get_summary(
        self,
        db,
        tenant_id: int
    ):

        result = (get_analytics(db=db,tenant_id=tenant_id))

        return {
            "total_questions": result[0] or 0,

            "avg_retrieval_ms":round(result[1] or 0,2),

            "avg_generation_ms": round(result[2] or 0,2),

            "avg_top_score": round(result[3] or 0,4),

            "avg_chunk_count": round(result[4] or 0,2),

            "avg_context_length":round(result[5] or 0,2),
        }