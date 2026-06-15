from sqlalchemy import func

from app.models.question_log_model import (
    QuestionLog,
)


def get_analytics(
    db,tenant_id: int
):

    result = (
        db.query(func.count(QuestionLog.id),

            func.avg(QuestionLog.retrieval_ms),

            func.avg(QuestionLog.generation_ms),

            func.avg(QuestionLog.top_score),

            func.avg(QuestionLog.chunk_count),

            func.avg(QuestionLog.context_length)).filter(QuestionLog.tenant_id==tenant_id).first()
    )

    return result