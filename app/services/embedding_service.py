from app.services.llm_service import LLMService

from app.models.chunk_embedding_model import (
    ChunkEmbedding,
)
import time

from app.repositories.chunk_embedding_repo import (
    get_latest_embedding,
    bulk_create_embeddings,
)
from google.genai.errors import ServerError

class EmbeddingService:

    MODEL_NAME = "gemini-embedding-2"

    def __init__(self):

        self.client = LLMService().client

    def generate_embedding(self,text: str) -> list[float]:

        max_retries = 5

        for attempt in range(max_retries):

            try:

                response = (
                    self.client.models.embed_content(
                        model=self.MODEL_NAME,
                        contents=text,
                    )
                )

                return response.embeddings[0].values

            except ServerError as e:

                if attempt == max_retries - 1:
                    raise

                wait_time = 2 ** attempt

                print(
                    f"Gemini unavailable. "
                    f"Retrying in {wait_time}s..."
                )

                time.sleep(wait_time)

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

            embedding = self.generate_embedding(
                chunk.content
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