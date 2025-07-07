import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma:2b"

def analyze_diff(diff):
    if not diff.strip():
        return "No meaningful changes detected."

    prompt = f"""You are a DevOps assistant. Analyze the following Git diff and provide:
1. Summary of code changes
2. Suggested deployment strategy
3. Testing impact
4. Any red flags or anti-patterns

Git Diff:
{diff}
"""
    return query_ollama(prompt)


def estimate_cost(infra_yaml):
    if not infra_yaml.strip():
        return "No infra content provided."

    prompt = f"""You are a cloud infrastructure cost expert. Based on the following infrastructure configuration, estimate the **monthly cost impact** assuming default pricing on AWS. Summarize your reasoning clearly.

Infrastructure Definition:
{infra_yaml}
"""
    return query_ollama(prompt)


def query_ollama(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False}
        )
        return response.json()["response"]
    except Exception as e:
        return f"⚠️ Failed to get AI response: {str(e)}"

