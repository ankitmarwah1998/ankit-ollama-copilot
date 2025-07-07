import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma:2b"

def analyze_diff(diff):
    if not diff.strip():
        return "⚠️ No code changes detected."

    prompt = f"""You are an AI DevOps assistant. Analyze the following Git diff and provide:
- Summary of code changes
- Suggested deployment strategy
- Any configuration/IaC impacts
- Testing recommendations
- Red flags or anti-patterns

Git Diff:
{diff}
"""
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        return response.json().get("response", "⚠️ AI returned no response.")
    return "⚠️ Failed to get AI response"

def estimate_cost(infra_content):
    if not infra_content.strip():
        return "⚠️ No infrastructure changes detected."

    prompt = f"""Estimate the monthly infrastructure cost based on this configuration:
{infra_content}

Provide base price, additional costs, and total monthly estimate. Assume common AWS pricing."""
    
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        return response.json().get("response", "⚠️ AI returned no cost estimation.")
    return "⚠️ Failed to get cost estimation"

