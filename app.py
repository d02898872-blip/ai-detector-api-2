from flask import Flask, jsonify, request

app = Flask(__name__)

def detector(score):
    if score >= 50:
        return {"result": "AI"}
    else:
        return {"result": "Human"}

@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    score = data.get("score")
    return jsonify(detector(score))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)