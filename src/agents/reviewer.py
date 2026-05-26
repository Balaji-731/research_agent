from src.agents.supervisor import LLM

class ReviewerAgent:
    def __init__(self):
        self.llm = LLM()

    def reviewer_agent(self, draft):
        prompt = f"""
        Review and improve the following report.

        Report:
        {draft}

        Check:
        - clarity
        - completeness
        - factual consistency
        - grammar

        Return the improved report.
        """

        return self.llm.invoke(prompt)