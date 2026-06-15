from app.repositories.eval_dataset_repo import (
    get_all_evaluation_cases,
)

from app.repositories.eval_result_repo import (
    create_evaluation_result,
)

from app.services.retrieval_service import (
    RetrievalService,
)
import re


class EvaluationRunnerService:

    def normalize(self,text: str):

        text = text.lower()

        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        text = re.sub(r"[^\w\s%]","",text)

        return text.strip()

    def run(self,db):

        test_cases = (get_all_evaluation_cases(db=db))

        retrieval_service = RetrievalService()

        passed = 0

        result_summary=[]

        for test_case in test_cases:

            results = (
                retrieval_service.retrieve(
                    db=db,
                    tenant_id=test_case.tenant_id,
                    query=test_case.question,
                    top_k=3,
                )
            )

            found = False
            top_chunk=None
            
            if results:
                top_chunk = results[0]["chunk"].content[:300]

            for result in results:

                

                expected = self.normalize(test_case.expected_answer)

                content = self.normalize(result["chunk"].content)

                if expected in content:
                    found = True
                    break

            if found:

                passed += 1
            result_summary.append({
                "question": test_case.question,
                "expected_answer": test_case.expected_answer,
                "passed": found,
                "top_chunk": top_chunk,
            })

        total = len(test_cases)

        recall = (
            passed / total
            if total > 0
            else 0
        )

        create_evaluation_result(
            db=db,
            total_cases=total,
            passed_cases=passed,
            recall_at_3=recall,
        )

        return {
            "total_cases": total,
            "passed_cases": passed,
            "recall_at_3": recall,
            "results": result_summary
        }