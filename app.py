from flask import Flask, request, jsonify
from model import analyze_diff, estimate_cost

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    if not data:
        return jsonify({"error": "❌ No JSON received"}), 400

    # If "diff" key is present, handle diff analysis
    if "diff" in data and data["diff"].strip():
        analysis = analyze_diff(data["diff"])
        return jsonify({"analysis": analysis})

    # If "infra" key is present, handle cost estimation
    if "infra" in data and data["infra"].strip():
        cost_estimate = estimate_cost(data["infra"])
        return jsonify({"analysis": cost_estimate})

    return jsonify({"error": "❌ No valid 'diff' or 'infra' provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

