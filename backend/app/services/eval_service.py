from app.repositories.eval_dataset_repo import (
    create_evaluation_case,
    get_all_evaluation_cases,
)
from app.repositories.eval_result_repo import get_all_evaluation_results

class EvaluationService:

    def create_case(
        self,
        db,
        tenant_id,
        question,
        expected_answer,
    ):

        return create_evaluation_case(
            db=db,
            tenant_id=tenant_id,
            question=question,
            expected_answer=expected_answer,
        )

    def get_cases(self,db):

        return get_all_evaluation_cases(db=db)
    
    def get_results(self,db):

        return get_all_evaluation_results(db=db)
    
    
from app.repositories.eval_result_repo import (
    get_evaluation_summary,
)


class EvaluationSummaryService:

    def get_summary(self,db):

        result = (get_evaluation_summary(db=db))

        return {
            "latest_recall":
                round(
                    result["latest_recall"],
                    4,
                ),

            "best_recall":
                round(
                    result["best_recall"],
                    4,
                ),

            "avg_recall":
                round(
                    result["avg_recall"],
                    4,
                ),
        }