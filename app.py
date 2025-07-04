from flask import Flask, request, jsonify
from datetime import datetime
import os
import requests

app = Flask(__name__)

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

OLLAMA_ENDPOINT = "http://localhost:11434/api/chat"  # Ollama running locally
OLLAMA_MODEL = "gemma:2b"

def query_ollama(diff_text):
    prompt = f"""
You are an AI assistant embedded in a CI/CD pipeline. A developer submitted the following code changes:

{diff_text}

Analyze the code diff and respond with:
1. A concise summary of the change.
2. Suggestions for testing.
3. Deployment strategy (e.g., staging only, full rollout).
4. Infrastructure changes required (if any).

Respond in markdown format under the heading '### AI Analysis'.
    """

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post(OLLAMA_ENDPOINT, json=payload)
        res.raise_for_status()
        response_json = res.json()
        reply = response_json["message"]["content"]
        return reply
    except Exception as e:
        return f"❌ Error fetching from Ollama: {str(e)}"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    diff = data.get("diff", "")

    if not diff:
        return jsonify({"error": "No diff provided"}), 400

    analysis = query_ollama(diff)
    response_json = {"analysis": analysis}

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = os.path.join(LOG_DIR, f"response_{timestamp}.json")
    md_path = os.path.join(LOG_DIR, f"response_{timestamp}.md")

    with open(json_path, "w") as f:
        import json
        json.dump(response_json, f, indent=2)

    with open(md_path, "w") as f:
        f.write(analysis)

    return jsonify(response_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

