from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    diff = data.get("diff", "")

    if not diff:
        return jsonify({"error": "No diff provided"}), 400

    # ✨ Mock response for now — replace with real Ollama call
    analysis = f"### AI Analysis\n\nThe diff contains {len(diff.splitlines())} lines.\n\n✅ Suggest: Review new print statement."
    response_json = {"analysis": analysis}

    # 📂 Save both .json and .md log files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = os.path.join(LOG_DIR, f"response_{timestamp}.json")
    md_path = os.path.join(LOG_DIR, f"response_{timestamp}.md")

    # Save raw JSON
    with open(json_path, "w") as f:
        import json
        json.dump(response_json, f, indent=2)

    # Save readable markdown
    with open(md_path, "w") as f:
        f.write(analysis)

    return jsonify(response_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

