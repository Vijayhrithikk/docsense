from app.services.llm_service import LLMService


class GenerationService:

    def __init__(self):

        self.llm_service = LLMService()

    def answer_question(
        self,
        question: str,
        context: str,
    ):

        prompt = f"""
You are answering questions using only
the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

        return self.llm_service.generate(prompt)