from flask import Flask, request, jsonify
from model import analyze_diff

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    diff = data.get("diff", "")
    result = analyze_diff(diff)
    return jsonify({"analysis": result})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

