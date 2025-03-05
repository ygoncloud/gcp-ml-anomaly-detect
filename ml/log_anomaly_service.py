import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify

# Load trained model
model = tf.keras.models.load_model("log_anomaly_model.h5")

app = Flask(__name__)

@app.route('/detect_anomaly', methods=['POST'])
def detect_anomaly():
    log_message = request.json['log']
    encoded_log = np.array([[hash(log_message) % 1000]])  # Simple encoding

    prediction = model.predict(encoded_log)
    anomaly_score = float(prediction[0][0])

    return jsonify({
        "log": log_message,
        "anomaly_score": anomaly_score,
        "is_anomalous": anomaly_score > 0.8
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

