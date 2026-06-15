from app.services.retrieval_service import RetrievalService
from app.services.generation_service import GenerationService
from app.repositories.question_log_repo import create_question_log

import time


class QuestionAnswerService:

    def __init__(self):

        self.retrieval_service = RetrievalService()

        self.generation_service = GenerationService()

    def answer(self,db,tenant_id:int ,question: str):

        retrieval_start = time.time()

        retrieved_chunks = (
            self.retrieval_service.retrieve(
                db=db,
                tenant_id=tenant_id,
                query=question,
                top_k=3,
            )
        )
        retrieval_ms = (time.time()- retrieval_start) *1000

        context = "\n\n".join(
            result["chunk"].content
            for result in retrieved_chunks
        )

        context_length = len(context)

        top_score = retrieved_chunks[0]["score"] if retrieved_chunks else 0

        chunk_count = len(retrieved_chunks)
        

        generation_start = time.time()
        answer = (
            self.generation_service.answer_question(
                question=question,
                context=context,
            )
        )
        generation_ms = (time.time()-generation_start)*1000

        create_question_log(

            db=db,
            tenant_id=tenant_id,
            question=question,
            answer=answer,
            retrieval_ms=retrieval_ms,
            generation_ms=generation_ms,
            top_score=top_score,
            chunk_count=chunk_count,
            context_length=context_length
            )

        return {
            "answer": answer,
            "sources":[
                 {
                "document_title": item["chunk"].document.title,
                "start_page": item["chunk"].start_page,
                "end_page": item["chunk"].end_page,
                "score": item["score"]
        }
        for item in retrieved_chunks
            ]
                
                }