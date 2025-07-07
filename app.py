from flask import Flask, request, jsonify
from model import analyze_diff, estimate_cost_from_infra

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON body received"}), 400

    if "diff" in data:
        diff = data["diff"]
        analysis = analyze_diff(diff)
        return jsonify({"analysis": analysis})

    elif "infra" in data:
        path = data.get("infra", "infra.yaml")
        analysis = estimate_cost_from_infra(path)
        return jsonify({"analysis": analysis})

    else:
        return jsonify({"error": "Invalid payload. Expected 'diff' or 'infra' key."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

