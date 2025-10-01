```python
from flask import Flask, request, jsonify
from pythonjsonlogger import jsonlogger
import logging

app = Flask(__name__)

# Configure structured logging
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

@app.route("/")
def home():
    logger.info("Home page accessed")
    return "🚀 Log Anomaly Detection Service is Running!"

@app.route("/log", methods=["POST"])
def receive_log():
    log_data = request.json
    logger.info("Received log", extra=log_data)
    return jsonify({"message": "Log received", "status": "success"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```
