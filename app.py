from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/')
def home():
    return jsonify({
        "message": "OrderAPI v1 is running!",
        "hostname": os.getenv("HOSTNAME")
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)