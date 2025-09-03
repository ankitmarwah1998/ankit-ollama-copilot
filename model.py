import requests
import json

def analyze_diff(diff_text: str) -> str:
    prompt = f"""
You are an AI DevOps assistant.
Analyze the following code diff and provide detailed response with:

1. Summary of intent
2. Recommended deployment strategy
3. Infrastructure impacted
4. Tests to run
5. Additional notes/risks

Diff:
{diff_text}
"""
    try:
        # Use stream=True to handle Ollama streamed JSON
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma:2b", "prompt": prompt},
            stream=True,
            timeout=300
        )
        response.raise_for_status()

        # Collect all "response" fields from streamed JSON lines
        full_output = ""
        for line in response.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    full_output += data["response"]
            except json.JSONDecodeError:
                # Ignore partial or invalid JSON lines
                continue

        return full_output.strip() if full_output else "⚠️ No analysis generated."

    except Exception as e:
        return f"❌ Error calling Ollama: {str(e)}"

