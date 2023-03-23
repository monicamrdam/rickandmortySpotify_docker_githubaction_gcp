from flask import Flask, jsonify

app = Flask(__name__)

# Routes
@app.route("/", methods=["GET"])
def ping():
    return jsonify({"response": "Hello Word!"})


# Start the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)