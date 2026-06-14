from app.services.retrieval_service import RetrievalService
from app.services.generation_service import GenerationService


class QuestionAnswerService:

    def __init__(self):

        self.retrieval_service = RetrievalService()

        self.generation_service = GenerationService()

    def answer(self,db,question: str):

        retrieved_chunks = (
            self.retrieval_service.retrieve(
                db=db,
                query=question,
                top_k=3,
            )
        )

        context = "\n\n".join(
            result["chunk"].content
            for result in retrieved_chunks
        )

        answer = (
            self.generation_service.answer_question(
                question=question,
                context=context,
            )
        )

        return {"answer": answer}