from src.workflows.graph import app

result = app.invoke(
    {
        "query": "Build an AI-powered resume screening system"
    }
)

print(result["final_report"])