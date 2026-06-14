from app.services.embedding_service import EmbeddingService
from app.models.chunk_embedding_model import ChunkEmbedding
import math
from app.models.chunk_model import Chunk
from app.services.tfidf_service import TFIDFService

class RetrievalService:

    def _compute_similarity(
        self,
        query_embedding: dict,
        chunk_embedding: dict,
    ):

        all_words = set(
            query_embedding.keys()
        ).union(
            chunk_embedding.keys()
        )

        dot_product = 0

        query_norm = 0

        chunk_norm = 0

        for word in all_words:

            q = query_embedding.get(word,0)

            c = chunk_embedding.get(word,0)

            dot_product += q * c

            query_norm += q * q

            chunk_norm += c * c

        if query_norm == 0 or chunk_norm == 0:

            return 0

        return dot_product / (
            math.sqrt(query_norm)
            * math.sqrt(chunk_norm))
    
    def retrieve(
    self,
    db,
    query: str,
    top_k: int = 5):
        
        tfidf_service = TFIDFService()

        all_embeddings = (db.query(ChunkEmbedding).all())

        idf = tfidf_service.compute_idf(
            [
                embedding.embedding
                for embedding in all_embeddings
            ]
        )
        
        query_embedding = (EmbeddingService()._generate_embedding(query))

        query_embedding = (
            tfidf_service.apply_tfidf(
                query_embedding,
                idf,
            )
        )
        scores =[]

        
        for embedding in all_embeddings:
        
            chunk_embedding = (
                tfidf_service.apply_tfidf(
                    embedding.embedding,
                    idf,
                )
            )

            score = self._compute_similarity(
                query_embedding,
                chunk_embedding,
            )
            
            if score <= 0:
                continue

            chunk = db.query(Chunk).filter(Chunk.id==embedding.chunk_id).first()
            # print(len(chunk.content))


            scores.append({
                "chunk": chunk,
                "score": score
            })

        scores.sort(key = lambda x: x["score"], reverse=True)

        return scores[:top_k]