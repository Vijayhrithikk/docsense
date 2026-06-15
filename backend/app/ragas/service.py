from app.services.generation_service import (
    GenerationService,
)


class RagasService:

    def __init__(self):

        self.generation_service = GenerationService()

    def evaluate(self,question: str,answer: str,context: str):

        prompt = f"""
You are evaluating a RAG system.

Question:
{question}

Context:
{context}

Answer:
{answer}

Score the following from 0 to 1:

1. Answer Relevancy
- Does the answer address the question?

2. Faithfulness
- Is the answer supported by the context?

Return ONLY:

answer_relevancy=<score>
faithfulness=<score>

Example:

answer_relevancy=0.92
faithfulness=0.88
"""

        result = (self.generation_service.generate(prompt))

        answer_relevancy = 0.0
        faithfulness = 0.0

        try:

            for line in result.splitlines():

                line = line.strip()

                if line.startswith("answer_relevancy="):

                    answer_relevancy = float(line.split("=")[1])

                if line.startswith("faithfulness="):
                    
                    faithfulness = float(line.split("=")[1])

        except Exception:

            pass

        return {
            "answer_relevancy": answer_relevancy,
            "faithfulness": faithfulness,
        }