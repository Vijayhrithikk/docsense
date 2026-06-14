from app.services.embedding_service import EmbeddingService
from app.models.chunk_embedding_model import ChunkEmbedding
from app.models.chunk_model import Chunk

import math
import time


class RetrievalService:

    def __init__(self):

        self.embedding_service = EmbeddingService()

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

        query_norm = math.sqrt(sum(q * q for q in query_embedding))

        chunk_norm = math.sqrt(
            sum(c * c for c in chunk_embedding))

        if (query_norm == 0 or chunk_norm == 0):
            return 0

        return (dot_product/ (query_norm* chunk_norm))

    def retrieve(
        self,
        db,
        query: str,
        top_k: int = 5,
    ):
        start = time.time()

        query_embedding = self.embedding_service.generate_embedding(query)

        print("Query embed time", time.time()-start)

        scores = []

        all_embeddings = (db.query(ChunkEmbedding).all())

        for embedding in all_embeddings:

            score = self._compute_similarity(
                query_embedding,
                embedding.embedding,
            )

            if score <= 0:
                continue

            chunk = (
                db.query(Chunk)
                .filter(
                    Chunk.id == embedding.chunk_id
                )
                .first()
            )

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

        return scores[:top_k]