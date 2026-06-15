from app.models.question_log_model import (
    QuestionLog,
)
from app.models.question_log_model import (
    QuestionLog,
)


def create_question_log(
    db,
    tenant_id,
    question,
    answer,
    retrieval_ms,
    generation_ms,
    top_score,
    chunk_count,
    context_length,
):

    log = QuestionLog(
        tenant_id=tenant_id,
        question=question,
        answer=answer,
        retrieval_ms=retrieval_ms,
        generation_ms=generation_ms,
        top_score=top_score,
        chunk_count=chunk_count,
        context_length=context_length
    )

    db.add(log)

    db.commit()

    db.refresh(log)

    return log





def get_question_history(
    db,
    tenant_id: int,
):

    return (
        db.query(QuestionLog)
        .filter(
            QuestionLog.tenant_id == tenant_id
        )
        .order_by(
            QuestionLog.created_at.desc()
        )
        .all()
    )


def get_question_by_id(
    db,
    question_id: int,
):

    return (
        db.query(QuestionLog)
        .filter(
            QuestionLog.id == question_id
        )
        .first()
    )