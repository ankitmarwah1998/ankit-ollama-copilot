import requests
import json

# ------------------------------
# Example functions to test AI
# ------------------------------
def add(a, b):
    """Add two numbers and log the operation."""
    print(f"Adding {a} + {b}")
    return a + b

def multiply(a, b):
    """Multiply two numbers, added for AI PR analysis testing."""
    print(f"Multiplying {a} * {b}")
    return a * b

# ------------------------------
# AI Analysis Function
# ------------------------------
def analyze_diff(diff_text: str) -> str:
    """
    Sends the diff to Ollama (gemma:2b) and returns AI analysis.
    Includes deployment strategy, infrastructure impact, cloud cost,
    tests to run, and additional notes.
    """
    prompt = f"""
You are an AI DevOps assistant.
Analyze the following code diff and provide a detailed response including:

1. Summary of intent of the change
2. Recommended deployment strategy
3. Infrastructure components impacted
4. Estimated cloud cost impact (CPU, memory, storage, network)
   - Provide approximate cost in USD assuming deployment on cloud (AWS/Google/Azure)
   - Include CPU hours, memory usage, storage cost if applicable
5. Tests to run before deploying
6. Additional notes / risks

Assume deployment on 1 small cloud instance (e.g., AWS t3.micro) for 24 hours.
Consider the impact of added functions or new features on cloud usage.

Diff:
{diff_text}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma:2b", "prompt": prompt},
            stream=True,
            timeout=300
        )
        response.raise_for_status()

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

# ------------------------------
# Optional: Test direct execution
# ------------------------------
if __name__ == "__main__":
    test_diff = """
+def add(a, b):
+    return a + b
+def multiply(a, b):
+    return a * b
"""
    result = analyze_diff(test_diff)
    print(result)

