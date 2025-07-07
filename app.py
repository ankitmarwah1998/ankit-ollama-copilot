from flask import Flask, request, jsonify
from model import generate_ai_suggestion, generate_cost_estimation

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    diff = data.get("diff", "")
    if not diff.strip():
        return jsonify({"analysis": "⚠️ No diff provided."}), 400
    result = generate_ai_suggestion(diff)
    return jsonify({"analysis": result})

@app.route("/estimate", methods=["POST"])
def estimate():
    data = request.get_json()
    infra = data.get("infra", "")
    if not infra.strip():
        return jsonify({"analysis": "⚠️ No infra content provided."}), 400
    result = generate_cost_estimation(infra)
    return jsonify({"analysis": result})

if __name__ == "__main__":
    app.run(debug=True)

