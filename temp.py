from app.db.database import SessionLocal


db =    SessionLocal()

from app.services.embedding_service import EmbeddingService

from app.models.chunk_model import Chunk

chunks = db.query(Chunk).all()

service = EmbeddingService()

service.ensure_embedding_exist(db=db, chunks=chunks)
