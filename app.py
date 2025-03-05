```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return "🚀 Log Anomaly Detection Service is Running!"

@app.route("/log", methods=["POST"])
def receive_log():
    log_data = request.json
    logging.info(f"Received log: {log_data}")
    return jsonify({"message": "Log received", "status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```
