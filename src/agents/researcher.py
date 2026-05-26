from src.agents.supervisor import LLM
from src.tools.web_search import WebSearch

class ResearcherAgent:
    def __init__(self):
        self.llm = LLM()
        self.search_tool = WebSearch()

    def research_agent(self, query):
        search_results = self.search_tool.search(query)

        prompt = f"""
        Analyze these search results.

        Search Results:
        {search_results}

        Extract:
        - key findings
        - important insights
        - trends
        """

        return self.llm.invoke(prompt)