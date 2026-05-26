from src.agents.supervisor import LLM

class EvaluatorAgent:
    def __init__(self):
        self.llm=LLM()
    
    def evaluate(self,query,research):
        prompt = f"""
        User Query:
        {query}

        Research:
        {research}

        Is this research sufficient?

        Return ONLY:
        GOOD

        or

        BAD
        """
        return self.llm.invoke(prompt)