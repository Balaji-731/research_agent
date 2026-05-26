from src.workflows.graph import app

result = app.invoke(
    {
        "query": "Future of AI Agents"
    }
)

print(result["final_report"])