from langchain_groq import ChatGroq
from src.config.settings import GROQ_API_KEY

class LLM:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=GROQ_API_KEY,
            temperature=0
        )

    def invoke(self, prompt):
        response = self.llm.invoke(prompt)
        return response.content