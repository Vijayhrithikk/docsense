from rank_bm25 import BM25Okapi


class BM25Service:

    def search(
        self,
        query: str,
        chunks: list,
        top_k: int = 5,
    ):

        if not chunks:
            return []

        corpus = [chunk.content.lower().split() for chunk in chunks]


        bm25 = BM25Okapi(corpus)

        scores = bm25.get_scores(query.lower().replace("?","").replace(",","").split())

        results = []

        for chunk, score in zip(chunks,scores):

            results.append(
                {
                    "chunk": chunk,
                    "score": float(score),
                }
            )

        results.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        return results[:top_k]