from sqlalchemy.orm import Session

from app.models.chunk_embedding_model import (
    ChunkEmbedding,
)


def bulk_create_embeddings(
    db: Session,
    embeddings: list[ChunkEmbedding],
):

    db.add_all(embeddings)

    db.commit()

    return embeddings


def get_latest_embedding(
    db: Session,
    chunk_id: int,
    model_name: str,
):

    return (
        db.query(ChunkEmbedding)
        .filter(
            ChunkEmbedding.chunk_id == chunk_id,
            ChunkEmbedding.model_name == model_name,
        ).order_by(ChunkEmbedding.created_at.desc()).first()
    )


def get_embeddings_by_model(
    db: Session,
    model_name: str,
):

    return (
        db.query(ChunkEmbedding)
        .filter(ChunkEmbedding.model_name == model_name).all()
    )