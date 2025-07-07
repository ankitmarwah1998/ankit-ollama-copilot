# 📁 File: model.py
import yaml
import ollama


def analyze_diff(diff: str) -> str:
    prompt = f"""
You are an AI code reviewer. Analyze the following code diff and:
1. Summarize the changes.
2. Suggest deployment strategies (e.g., rolling, blue-green, canary) based on the changes.
3. Suggest required infrastructure changes or scaling needs if any.
4. Identify any potential anti-patterns or risky changes.
5. Recommend any related tests.

Diff:
{diff}
"""
    try:
        response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        return f"❗Failed to get AI response: {e}"


def estimate_cost(infra_yaml: str) -> str:
    try:
        infra = yaml.safe_load(infra_yaml)
    except yaml.YAMLError as e:
        return f"❗Failed to parse YAML: {e}"

    prompt = f"""
You are an expert DevOps cost estimator. Based on the following infrastructure definition in YAML, estimate the monthly AWS cost. Include EC2, RDS, S3, Kubernetes nodes, monitoring tools, networking, and storage. Present your answer in a neat markdown format:

Infra:
{infra_yaml}
"""
    try:
        response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        return f"❗Failed to get cost estimation: {e}"

