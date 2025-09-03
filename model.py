import requests
import json

def analyze_diff(diff_text: str) -> str:
    prompt = f"""
You are an AI DevOps assistant.
Analyze the following code diff and provide detailed response including:

1. Summary of intent of the change
2. Recommended deployment strategy
3. Infrastructure components impacted
4. Estimated cloud cost impact (CPU, memory, storage, network)
5. Tests to run before deploying
6. Additional notes / risks

Diff:
{diff_text}
"""
    try:
        # Streamed request to Ollama
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma:2b", "prompt": prompt},
            stream=True,
            timeout=300
        )
        response.raise_for_status()

        # Collect all "response" fields from streamed JSON
        full_output = ""
        for line in response.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    full_output += data["response"]
            except json.JSONDecodeError:
                continue

        return full_output.strip() if full_output else "⚠️ No analysis generated."

    except Exception as e:
        return f"❌ Error calling Ollama: {str(e)}"

