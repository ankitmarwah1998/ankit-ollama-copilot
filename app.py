# app.py
from flask import Flask, request, jsonify
from model import analyze_diff

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    diff = data.get("diff", "")
    if not diff:
        return jsonify({"message": "No diff provided."}), 400

    analysis = analyze_diff(diff)
    return jsonify({"message": analysis})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

