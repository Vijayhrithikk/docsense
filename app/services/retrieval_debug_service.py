from app.services.retrieval_service import (
    RetrievalService,
)


class RetrievalDebugService:

    def debug(self,db,tenant_id,query,):

        results = (
            RetrievalService()
            .retrieve(
                db=db,
                tenant_id=tenant_id,
                query=query,
                top_k=5,
            )
        )

        return [
            {
                "score": item["score"],

                "start_page": item["chunk"].start_page,

                "document_id": item["chunk"].document_id,

                "end_page":item["chunk"].end_page,

                "content":item["chunk"].content[:500]
            }
            for item in results
        ]