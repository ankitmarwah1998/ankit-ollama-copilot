import requests
import json
from datetime import datetime
import os

def analyze_diff(diff: str) -> str:
    if not diff.strip():
        return "No diff provided."

    prompt = f"""
You are a DevOps AI assistant. Analyze the following git diff and:

1. Summarize the intent of the change.
2. Recommend a deployment strategy (blue-green, canary, rolling, etc.) with justification.
3. List infrastructure components impacted (e.g., frontend, backend, database).
4. Suggest tests to run before deploying.

Git Diff:
{diff}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    analysis = result.get("response", "No response from AI.")

    # Save to logs with timestamp
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"logs/response_{timestamp}.json", "w") as f:
        json.dump({
            "timestamp": timestamp,
            "diff": diff,
            "response": analysis
        }, f, indent=2)

    return analysis

