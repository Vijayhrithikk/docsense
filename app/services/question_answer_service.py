from app.services.retrieval_service import RetrievalService
from app.services.generation_service import GenerationService

import time


class QuestionAnswerService:

    def __init__(self):

        self.retrieval_service = RetrievalService()

        self.generation_service = GenerationService()

    def answer(self,db,question: str):

        start = time.time()

        retrieved_chunks = (
            self.retrieval_service.retrieve(
                db=db,
                query=question,
                top_k=3,
            )
        )
        print("Retrieval time", time.time()- start)

        context = "\n\n".join(
            result["chunk"].content
            for result in retrieved_chunks
        )
        start = time.time()

        answer = (
            self.generation_service.answer_question(
                question=question,
                context=context,
            )
        )
        print("Retrieval time", time.time()- start)

        return {
            "answer": answer,
            "sources":[
                 {
                "chunk_id": item["chunk"].id,
                "score": item["score"]
        }
        for item in retrieved_chunks
            ]
                
                }