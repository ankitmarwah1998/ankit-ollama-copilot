import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gemma:2b"

def analyze_diff(diff):
    if not diff.strip():
        return "⚠️ No meaningful code changes detected in this PR."

    prompt = f"""
You are an AI DevOps assistant embedded in a CI/CD pipeline.

Given the following git diff, perform the following:
- Summarize the changes
- Suggest appropriate deployment strategies (e.g., blue/green, canary, rolling, etc.)
- Recommend tests or rollback plans
- Detect risky code (e.g., database migrations, config changes)
- Output in GitHub Markdown format with bullet points, emojis, and bold sections.

Git Diff:
{diff}
"""

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        result = response.json()
        return result.get("response", "⚠️ No response from AI model.")
    except Exception as e:
        return f"❌ AI suggestion failed: {str(e)}"

