import subprocess
import json

def analyze_diff(diff_text):
    if not diff_text.strip():
        return "⚠️ No code changes detected."

    try:
        ollama_prompt = f"Analyze the following Git diff and suggest improvements, testing strategies, red flags, and infrastructure recommendations:\n\n{diff_text}"
        result = subprocess.run(
            ["ollama", "run", "gemma:2b"],
            input=ollama_prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30
        )

        output = result.stdout.decode().strip()
        if output:
            return output
        else:
            return "⚠️ AI response was empty. Please verify Ollama is running."
    except Exception as e:
        return f"⚠️ Failed to analyze diff: {str(e)}"

def estimate_cost(infra_text):
    if not infra_text.strip():
        return "⚠️ Infra file is empty or missing."

    try:
        ollama_prompt = f"""Analyze the following infrastructure configuration and estimate the monthly cost impact. Use realistic assumptions and include service-wise breakdown. Output in markdown:\n\n{infra_text}"""
        result = subprocess.run(
            ["ollama", "run", "gemma:2b"],
            input=ollama_prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30
        )

        output = result.stdout.decode().strip()
        if output:
            return output
        else:
            return "⚠️ AI returned an empty response for cost estimation."
    except Exception as e:
        return f"⚠️ Failed to estimate cost: {str(e)}"

