from app.models.document_model import Document
from app.models.chunk_model import Chunk
from app.models.question_log_model import QuestionLog
from app.models.eval_result_model import EvaluationResult


def get_metrics(
    db,
):

    document_count = (
        db.query(Document)
        .count()
    )

    chunk_count = (
        db.query(Chunk)
        .count()
    )

    question_count = (
        db.query(QuestionLog)
        .count()
    )

    evaluation_count = (
        db.query(EvaluationResult)
        .count()
    )

    return (
        document_count,
        chunk_count,
        question_count,
        evaluation_count,
    )