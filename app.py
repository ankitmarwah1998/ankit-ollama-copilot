from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    diff = data.get("diff", "")
    result = {
        "summary": "Some summary",
        "deployment_strategy": "Rolling",
        "test_strategy": "Integration",
        "infra_change": "None"
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

