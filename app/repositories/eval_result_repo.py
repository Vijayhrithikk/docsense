from sqlalchemy.orm import Session

from app.models.eval_result_model import (
    EvaluationResult,
)


def create_evaluation_result(
    db: Session,
    total_cases: int,
    passed_cases: int,
    recall_at_3: float,
):

    result = EvaluationResult(
        total_cases=total_cases,
        passed_cases=passed_cases,
        recall_at_3=recall_at_3,
    )

    db.add(result)

    db.commit()

    db.refresh(result)

    return result


def get_all_evaluation_results(db: Session):

    return (db.query(EvaluationResult).order_by(EvaluationResult.created_at.desc()).all())