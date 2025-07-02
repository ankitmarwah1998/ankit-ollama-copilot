from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    diff = data.get("diff", "")
    print("Received diff length:", len(diff))
    return jsonify({"message": f"Received diff of length {len(diff)}"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

