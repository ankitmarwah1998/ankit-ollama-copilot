from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    # Optional: log or print the diff
    return jsonify({"analysis": "This is a dummy analysis result."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

