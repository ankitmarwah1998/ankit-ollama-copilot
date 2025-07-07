from flask import Flask, request, jsonify
from model import analyze_diff, estimate_cost

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        diff = data.get("diff", "")
        result = analyze_diff(diff)
        return jsonify({"analysis": result})
    except Exception as e:
        return jsonify({"analysis": f"⚠️ Failed to get AI response: {str(e)}"}), 400

@app.route("/estimate", methods=["POST"])
def estimate():
    try:
        data = request.get_json()
        yaml_content = data.get("infra", "")
        result = estimate_cost(yaml_content)
        return jsonify({"analysis": result})
    except Exception as e:
        return jsonify({"analysis": f"❌ No cost estimation: {str(e)}"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

