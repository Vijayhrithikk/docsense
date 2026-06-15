from app.services.llm_service import (
    LLMService
)


class GenerationService:

    def __init__(self):

        self.llm_service = LLMService()

    def generate(self,prompt: str):

        return (self.llm_service.generate(prompt))

    def answer_question(self,question: str,context: str):

        prompt = f"""
You are a document assistant.

Answer the user's question using only the provided context.

If the answer cannot be found in the context, say:

"I could not find that information in the uploaded documents."

Context:

{context}

Question:

{question}

Answer:
"""

        return self.generate(prompt)