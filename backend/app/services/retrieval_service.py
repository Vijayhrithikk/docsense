from app.services.embedding_service import EmbeddingService
from app.services.bm25_service import BM25Service

from app.models.chunk_embedding_model import ChunkEmbedding
from app.models.chunk_model import Chunk
from app.models.document_model import Document

import math
import time


class RetrievalService:

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.bm25_service = BM25Service()

    def _compute_similarity(
        self,
        query_embedding: list[float],
        chunk_embedding: list[float],
    ):

        dot_product = sum(
            q * c
            for q, c in zip(
                query_embedding,
                chunk_embedding,
            )
        )

        query_norm = math.sqrt(
            sum(
                q * q
                for q in query_embedding
            )
        )

        chunk_norm = math.sqrt(
            sum(
                c * c
                for c in chunk_embedding
            )
        )

        if (
            query_norm == 0
            or chunk_norm == 0
        ):
            return 0

        return (
            dot_product/(query_norm* chunk_norm)
        )

    def retrieve(
        self,
        db,
        tenant_id: int,
        query: str,
        top_k: int = 5,
    ):

        start = time.time()

        query_embedding = (self.embedding_service.generate_embedding(query))

        print(
            "Query embed time",
            time.time() - start,
        )

        chunks = (
            db.query(Chunk)
            .join(
                Document,
                Document.id == Chunk.document_id,
            )
            .filter(
                Document.tenant_id == tenant_id
            )
            .all()
        )

        chunk_map = {
            chunk.id: chunk
            for chunk in chunks
        }

        all_embeddings = (
            db.query(ChunkEmbedding)
            .join(
                Chunk,
                Chunk.id == ChunkEmbedding.chunk_id,
            )
            .join(
                Document,
                Document.id == Chunk.document_id,
            )
            .filter(
                Document.tenant_id == tenant_id
            )
            .all()
        )

        scores = []

        for embedding in all_embeddings:

            score = (
                self._compute_similarity(
                    query_embedding,
                    embedding.embedding,
                )
            )

            if score < 0:
                continue

            chunk = chunk_map.get(embedding.chunk_id)

            if not chunk:
                continue

            scores.append(
                {
                    "chunk": chunk,
                    "score": score,
                }
            )

        scores.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        embedding_results = scores[:20]

        bm25_results = (
            self.bm25_service.search(
                query=query,
                chunks=chunks,
                top_k=20,
            )
        )

        rrf_scores = {}

        K = 60

        for rank, item in enumerate(
            embedding_results,
            start=1,
        ):

            chunk_id = (item["chunk"].id)

            rrf_scores.setdefault(
                chunk_id,
                {
                    "chunk": item["chunk"],
                    "score": 0,
                },
            )

            rrf_scores[chunk_id]["score"] += (1 / (K + rank))

        for rank, item in enumerate(
            bm25_results,
            start=1,
        ):

            chunk_id = item["chunk"].id

            rrf_scores.setdefault(
                chunk_id,
                {
                    "chunk": item["chunk"],
                    "score": 0,
                },
            )

            rrf_scores[chunk_id]["score"] += (1 / (K + rank))

        hybrid_results = list(rrf_scores.values())

        hybrid_results.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        print("\nRRF RESULTS\n")

        for item in hybrid_results[:5]:

            print(item["score"])

            print(item["chunk"].start_page,item["chunk"].end_page)

            print(item["chunk"].content[:300])

            print("=" * 50)

        return hybrid_results[:top_k]