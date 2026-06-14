from app.models.chunk_model import Chunk


def bulk_create_chunks(
    db,
    document_id: int,
    chunks: list[dict],
):

    records = []

    for chunk in chunks:

        records.append(Chunk(
                document_id=document_id,
                start_page=chunk["start_page"],
                end_page=chunk["end_page"],
                content=chunk["content"],
            )
        )

    db.add_all(records)

    db.commit()

    return records