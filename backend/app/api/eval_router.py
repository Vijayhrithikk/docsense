from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.eval_service import (
    EvaluationService,
    EvaluationSummaryService
)

from app.schemas.eval_schema import (
    EvaluationCaseCreate,
    EvaluationCaseResponse,
    EvaluationRunResponse,
    EvaluationResultResponse,
    EvaluationSummaryResponse
)

from app.services.eval_runner_service import EvaluationRunnerService

router = APIRouter(
    prefix="/evaluation",
    tags=["Evaluation"],
)

service = EvaluationService()


@router.post("/cases",response_model=EvaluationCaseResponse)
def create_case(
    request: EvaluationCaseCreate,
    db: Session = Depends(get_db),
):

    return service.create_case(
        db=db,
        tenant_id=request.tenant_id,
        question=request.question,
        expected_answer=request.expected_answer,
    )


@router.get("/cases",response_model=list[EvaluationCaseResponse])
def get_cases(db: Session = Depends(get_db)):

    return service.get_cases(db=db)


runner = EvaluationRunnerService()

@router.post("/run", response_model=EvaluationRunResponse)
def run_eval(db: Session = Depends(get_db)):
    return runner.run(db=db)

@router.get("/results",response_model=list[EvaluationResultResponse])
def get_results(db: Session=Depends(get_db)):
    return service.get_results(db=db)


summary_service = EvaluationSummaryService()


@router.get(
    "/summary",
    response_model=
    EvaluationSummaryResponse,
)
def get_summary(
    db: Session = Depends(get_db),
):

    return (summary_service.get_summary(db=db))