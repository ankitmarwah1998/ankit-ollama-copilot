import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma:2b"

def generate_ai_suggestion(diff):
    prompt = f"""
You are an AI DevOps assistant. Analyze the following Git diff and provide:
- Summary of code changes
- Suggested deployment strategy
- Configuration/IaC changes
- Testing recommendations
- Red flags or anti-patterns

Git Diff:
{diff}
"""
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    if response.status_code == 200:
        return response.json().get("response", "⚠️ AI returned empty response.")
    return "⚠️ Failed to get AI response"

def generate_cost_estimation(infra_content):
    prompt = f"""
Estimate monthly infrastructure cost based on this IaC config:

{infra_content}

Include base price breakdown, additional costs (networking, monitoring), and total estimate.
"""
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    if response.status_code == 200:
        return response.json().get("response", "⚠️ AI returned empty cost estimate.")
    return "⚠️ Failed to get cost estimation"

