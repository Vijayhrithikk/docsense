from sqlalchemy.orm import Session

from app.models.eval_result_model import (
    EvaluationResult,
)

from sqlalchemy import func


def create_evaluation_result(
    db: Session,
    total_cases: int,
    passed_cases: int,
    recall_at_3: float,
    answer_relevancy: float,
    faithfulness: float 

):

    result = EvaluationResult(
        total_cases=total_cases,
        passed_cases=passed_cases,
        recall_at_3=recall_at_3,
        answer_relevancy=answer_relevancy,
        faithfulness=faithfulness
    )

    db.add(result)

    db.commit()

    db.refresh(result)

    return result


def get_all_evaluation_results(db: Session):

    return (db.query(EvaluationResult).order_by(EvaluationResult.created_at.desc()).all())

def get_evaluation_summary(
    db,
):

    latest = (
        db.query(EvaluationResult)
        .order_by(EvaluationResult.created_at.desc()).first()
    )

    best_recall = (
        db.query(func.max(EvaluationResult.recall_at_3))
        .scalar()
    )

    avg_recall = (
        db.query(func.avg(EvaluationResult.recall_at_3))
        .scalar()
    )

    return {
        "latest_recall":
            latest.recall_at_3
            if latest else 0,

        "best_recall":
            best_recall or 0,

        "avg_recall":
            avg_recall or 0,
    }