from src.agents.supervisor import LLM

class QueryRefiner:
    def __init__(self):
        self.llm=LLM()

    def refine(self,original_query,research_history):
        research="\n".join(research_history)
        prompt = f"""
        Original Query:
        {original_query}

        Research Collected:
        {research}

        Generate a better and more specific
        search query.

        Return only the query.
        """
        return self.llm.invoke(prompt)