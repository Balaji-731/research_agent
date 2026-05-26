from tavily import TavilyClient
from src.config.settings import TAVILY_API_KEY

class WebSearch:
    def __init__(self):
        self.client = TavilyClient(
            api_key=TAVILY_API_KEY
        )

    def search(self, query):
        response = self.client.search(
            query=query,
            max_results=5
        )

        results = response["results"]

        combined = ""

        for result in results:
            combined += result["content"] + "\n\n"

        return combined