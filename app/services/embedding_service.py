from app.repositories.chunk_embedding_repo import (
    get_latest_embedding,
    bulk_create_embeddings
)

from app.models.chunk_embedding_model import ChunkEmbedding

class EmbeddingService:

    MODEL_NAME= "fake-v1"

    def ensure_embedding_exist(self,db,chunks):

        embeddings_to_create = []

        for chunk in chunks:

            existing = get_latest_embedding(db=db,chunk_id=chunk.id, model_name=self.MODEL_NAME)

            if existing:
                print("Already existing")
                continue 

            fake_embedding = self._generate_embedding(chunk.content)

            embeddings_to_create.append(ChunkEmbedding(
                chunk_id=chunk.id,
                model_name = self.MODEL_NAME,
                embedding = fake_embedding)
                )
            print("embedding created")
        print("Total embedding", len(embeddings_to_create))
            
        if embeddings_to_create:

            bulk_create_embeddings(db=db,embeddings=embeddings_to_create)

    def _generate_embedding(self, text: str):

        words = text.lower().split()

        embedding = {}

        for word in words:

            embedding[word] = embedding.get(word,0)+1

        return embedding
