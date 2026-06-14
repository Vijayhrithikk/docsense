from sentence_transformers import SentenceTransformer

from app.models.chunk_embedding_model import (
    ChunkEmbedding,
)

from app.repositories.chunk_embedding_repo import (
    get_latest_embedding,
    bulk_create_embeddings,
)


class EmbeddingService:

    MODEL_NAME = (
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    _model = None

    def __init__(self):

        if EmbeddingService._model is None:

            print("Loading embedding model...")

            EmbeddingService._model = (SentenceTransformer(self.MODEL_NAME))

        self.model = EmbeddingService._model

    def generate_embedding(
        self,
        text: str,
    ) -> list[float]:

        embedding = self.model.encode(
            text,
            convert_to_numpy=True,
        )

        return embedding.tolist()

    def ensure_embedding_exist(
        self,
        db,
        chunks,
    ):

        embeddings_to_create = []

        for chunk in chunks:

            existing = get_latest_embedding(
                db=db,
                chunk_id=chunk.id,
                model_name=self.MODEL_NAME,
            )

            if existing:
                continue

            embedding = (
                self.generate_embedding(
                    chunk.content
                )
            )

            embeddings_to_create.append(
                ChunkEmbedding(
                    chunk_id=chunk.id,
                    model_name=self.MODEL_NAME,
                    embedding=embedding,
                )
            )

        if embeddings_to_create:

            bulk_create_embeddings(
                db=db,
                embeddings=embeddings_to_create,
            )