from typing import TypedDict,List

from langgraph.graph import StateGraph, END

from src.agents.planner import PlannerAgent
from src.agents.researcher import ResearcherAgent
from src.agents.research_summarizer import ResearchSummarizer
from src.agents.evaluator import EvaluatorAgent
from src.agents.query_refiner import QueryRefiner
from src.agents.writer import WriterAgent
from src.agents.reviewer import ReviewerAgent


planner = PlannerAgent()
researcher = ResearcherAgent()
evaluator = EvaluatorAgent()
refiner=QueryRefiner()
summarizer=ResearchSummarizer()
writer = WriterAgent()
reviewer = ReviewerAgent()


class AgentState(TypedDict):
    query: str
    current_query: str
    query_history: List[str]
    plan: str
    research_history: List[str]
    research_summary:  str
    status: str
    retry_count: int
    draft: str
    final_report: str


def planner_node(state):
    plan = planner.planner_agent(
        state["query"]
    )

    return {"plan": plan,"current_query":state["query"]}


def research_node(state):
    research = researcher.research_agent(
        state["current_query"]
    )
    history=state.get("research_history",[])
    history.append(research)
    searches=state.get("query_history",[])
    searches.append(state["current_query"])
    return {"research_history": history,"query_history":searches}

def summarize_node(state):
    summary=summarizer.summarize(
        state["research_history"]
    )
    return {"research_summary":summary}

def evaluator_node(state):
    latest_research=state["research_history"][-1]
    status=evaluator.evaluate(
        state["query"],
        latest_research
    )
    retry_count=state.get("retry_count",0)
    if status=="BAD":
        retry_count+=1

    return {"status":status,"retry_count":retry_count}

def refiner_node(state):
    new_query=refiner.refine(
        state["query"],
        state["research_history"]
    )
    return {"current_query":new_query}

def evaluation_router(state):
    if state["status"]=="GOOD":
        return "summarizer"
    if state["retry_count"]>=3:
        return "summarizer"
    return "refiner"

def writer_node(state):
    draft = writer.writer_agent(
        state["plan"],
        state["research_summary"]
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
graph.add_node("summarizer",summarize_node)
graph.add_node("evaluator",evaluator_node)
graph.add_node("refiner",refiner_node)
graph.add_node("writer", writer_node)
graph.add_node("reviewer", reviewer_node)

graph.set_entry_point("planner")

graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "evaluator")
graph.add_conditional_edges("evaluator",evaluation_router,{
    "summarizer": "summarizer",
    "refiner":"refiner"
})
graph.add_edge("refiner","researcher")
graph.add_edge("summarizer","writer")
graph.add_edge("writer", "reviewer")
graph.add_edge("reviewer", END)

app = graph.compile()

png_data = app.get_graph().draw_mermaid_png()

with open("agent_graph.png", "wb") as f:
    f.write(png_data)

print("Graph saved as agent_graph.png")