from flask import Flask, request, jsonify
from model import analyze_diff

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    diff = data.get("diff", "")

    if not diff.strip():
        return jsonify({"error": "No diff provided"}), 400

    try:
        response = analyze_diff(diff)
        return jsonify({"analysis": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

