from typing import TypedDict

from langgraph.graph import StateGraph, END

from src.agents.planner import PlannerAgent
from src.agents.researcher import ResearcherAgent
from src.agents.writer import WriterAgent
from src.agents.reviewer import ReviewerAgent


planner = PlannerAgent()
researcher = ResearcherAgent()
writer = WriterAgent()
reviewer = ReviewerAgent()


class AgentState(TypedDict):
    query: str
    plan: str
    research: str
    draft: str
    final_report: str


def planner_node(state):
    plan = planner.planner_agent(
        state["query"]
    )

    return {"plan": plan}


def research_node(state):
    research = researcher.research_agent(
        state["query"]
    )

    return {"research": research}


def writer_node(state):
    draft = writer.writer_agent(
        state["plan"],
        state["research"]
    )

    return {"draft": draft}


def reviewer_node(state):
    final_report = reviewer.reviewer_agent(
        state["draft"]
    )

    return {"final_report": final_report}


graph = StateGraph(AgentState)

graph.add_node("planner", planner_node)
graph.add_node("researcher", research_node)
graph.add_node("writer", writer_node)
graph.add_node("reviewer", reviewer_node)

graph.set_entry_point("planner")

graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "writer")
graph.add_edge("writer", "reviewer")
graph.add_edge("reviewer", END)

app = graph.compile()