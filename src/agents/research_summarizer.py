from src.agents.supervisor import LLM

class ResearchSummarizer:
    def __init__(self):
        self.llm=LLM()

    def summarize(self,history):
        combined="\n\n".join(history)
        prompt = f"""
        Combine all findings.

        Research:
        {combined}

        Remove duplicates.
        Extract key insights.
        """
        return self.llm.invoke(prompt)