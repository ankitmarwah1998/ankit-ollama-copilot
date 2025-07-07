from flask import Flask, request, jsonify
from model import analyze_diff  # Assuming you use a function to call Ollama or process the diff

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    diff = data.get("diff", "")

    if not diff:
        return jsonify({"error": "No diff provided"}), 400

    # ✅ Call AI logic here
    result = analyze_diff(diff)  # Replace this with your actual logic

    return jsonify({"analysis": result})  # ✅ This is what GitHub Action expects

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

