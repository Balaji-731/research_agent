from src.agents.supervisor import LLM

class PlannerAgent:
    def __init__(self):
        self.llm = LLM()

    def planner_agent(self, user_query):
        prompt = f"""
        You are a planning agent.

        User Query:
        {user_query}

        Create:
        - objectives
        - research areas
        - execution plan
        """

        return self.llm.invoke(prompt)