import math


class TFIDFService:

    def compute_idf(
        self,
        chunk_embeddings: list[dict],
    ):

        total_documents = len(chunk_embeddings)

        document_frequency = {}

        for embedding in chunk_embeddings:

            for word in embedding.keys():

                document_frequency[word] = (document_frequency.get(word,0)+ 1)

        idf = {}

        for word, count in (document_frequency.items()):

            idf[word] = math.log(
                total_documents
                / count
            )

        return idf
    
    def apply_tfidf(
        self,
        embedding: dict,
        idf: dict,):

        weighted = {}

        for word, tf in (embedding.items()):

            weighted[word] = (tf*idf.get(word, 0))

        return weighted
