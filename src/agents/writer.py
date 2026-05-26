from src.agents.supervisor import LLM

class WriterAgent:
    def __init__(self):
        self.llm = LLM()

    def writer_agent(self, plan, research_summary):
        prompt = f"""
        Create a detailed report.

        Plan:
        {plan}

        Research Summary:
        {research_summary}

        Generate:
        - introduction
        - analysis
        - insights
        - conclusion
        """

        return self.llm.invoke(prompt)