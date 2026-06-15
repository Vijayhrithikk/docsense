from app.repositories.question_log_repo import (
    get_question_history,
    get_question_by_id,
)


class QuestionHistoryService:

    def get_history(
        self,
        db,
        tenant_id: int,
    ):

        return get_question_history(
            db=db,
            tenant_id=tenant_id,
        )

    def get_question(
        self,
        db,
        question_id: int,
    ):

        return get_question_by_id(
            db=db,
            question_id=question_id,
        )