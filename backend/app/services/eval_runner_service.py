from app.repositories.eval_dataset_repo import (
    get_all_evaluation_cases,
)

from app.repositories.eval_result_repo import (
    create_evaluation_result,
)

from app.services.retrieval_service import (
    RetrievalService,
)
from app.services.question_answer_service import QuestionAnswerService
from app.ragas.service import RagasService
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
        # qa_service = QuestionAnswerService()
        # ragas_service = RagasService()

        passed = 0

        result_summary=[]

        # total_relevancy = 0
        # total_faithfulness = 0


        for test_case in test_cases:

            

            results = (
                retrieval_service.retrieve(
                    db=db,
                    tenant_id=test_case.tenant_id,
                    query=test_case.question,
                    top_k=3,
                )
            )

            # context = "\n\n".join(result["chunk"].content for result in results)
            # qa_result = qa_service.answer(db=db,tenant_id=test_case.tenant_id,question=test_case.question)
            # answer = qa_result["answer"]
            # ragas_scores = ragas_service.evaluate(question=test_case.question,answer=answer,context=context)
            # total_relevancy+= ragas_scores["answer_relevancy"]
            # total_faithfulness += ragas_scores["faithfulness"]

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

        # avg_relevancy = (total_relevancy/total) if total>0 else 0
        # avg_faithfulness = (total_faithfulness/total) if total >0 else 0

        create_evaluation_result(
            db=db,
            total_cases=total,
            passed_cases=passed,
            recall_at_3=recall,
            answer_relevancy=0,
            faithfulness=0
        )

        return {
            "total_cases": total,
            "passed_cases": passed,
            "recall_at_3": recall,
            "relevancy": 0,
            "faithfulness": 0,
            "results": result_summary
        }