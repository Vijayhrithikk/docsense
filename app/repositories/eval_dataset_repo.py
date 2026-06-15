from sqlalchemy.orm import Session

from app.models.evaluation_dataset_model import (
    EvaluationDataset,
)


def create_evaluation_case(
    db: Session,
    tenant_id: int,
    question: str,
    expected_answer: str,
):

    case = EvaluationDataset(
        tenant_id=tenant_id,
        question=question,
        expected_answer=expected_answer,
    )

    db.add(case)

    db.commit()

    db.refresh(case)

    return case


def get_all_evaluation_cases(
    db: Session,
):

    return (db.query(EvaluationDataset).all())