from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.question import (
    AskQuestionRequest,
    AskQuestionResponse,
)

from app.services.question_answer_service import (
    QuestionAnswerService,
)
from app.services.question_answer_service import QuestionAnswerService
from app.services.question_history_service import QuestionHistoryService
from app.schemas.question import QuestionHistoryItem
from app.services.retrieval_debug_service import RetrievalDebugService

router = APIRouter(
    prefix="/questions",
    tags=["questions"],
)


@router.post(
    "/ask",
    response_model=AskQuestionResponse,
)
def ask_question(
    request: AskQuestionRequest,
    db: Session = Depends(get_db),
):

    service = QuestionAnswerService()

    result = service.answer(
        db=db,
        tenant_id=request.tenant_id,
        question=request.question,
    )

    return result

@router.get(
    "/history/{tenant_id}",
    response_model=list[QuestionHistoryItem],
)
def get_question_history(
    tenant_id: int,
    db: Session = Depends(get_db),
):

    service = QuestionHistoryService()

    return service.get_history(
        db=db,
        tenant_id=tenant_id,
    )

@router.get(
    "/history/question/{question_id}",
    response_model=QuestionHistoryItem,
)
def get_question(
    question_id: int,
    db: Session = Depends(get_db),
):

    service = QuestionHistoryService()

    return service.get_question(
        db=db,
        question_id=question_id,
    )


@router.get("/debug/retrieval")
def debug_retrieval(
    tenant_id: int,
    query: str,
    db: Session = Depends(get_db),
):

    return (
        RetrievalDebugService()
        .debug(
            db=db,
            tenant_id=tenant_id,
            query=query,
        )
    )