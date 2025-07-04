from flask import request
import requests

def analyze_diff(diff):
    system_prompt = """You are an AI DevOps Assistant. Given a Git diff:
1. 🔍 Summarize the change in simple terms.
2. 🚀 Suggest an appropriate deployment strategy:
   - rolling update
   - canary release
   - blue-green deployment
   - test-only
   - manual approval needed
3. ⚙️ Mention if there are infrastructure/config changes.
Be clear and concise. Output the response in Markdown format with appropriate emojis and headings.
"""

    # Combine prompt and diff
    full_prompt = f"{system_prompt}\n\nGit Diff:\n{diff}"

    # Send request to Ollama API
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": full_prompt,
            "stream": False
        }
    )

    # Extract response
    result = response.json()
    return result.get("response", "❌ No response from model")

