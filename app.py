from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    diff = data.get("diff", "")
    
    if not diff:
        return jsonify({"error": "No diff provided"}), 400

    return jsonify({"message": f"Received diff of length {len(diff)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

