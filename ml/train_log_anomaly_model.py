import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import LabelEncoder

# Check if logs.csv exists
LOG_FILE = "logs/log_sample.csv"

if not os.path.exists(LOG_FILE):
    print(f"🚨 Log file '{LOG_FILE}' not found! Generating sample logs...")
    with open(LOG_FILE, "w") as file:
        file.write("timestamp,loglevel,message\n")
        file.write("2025-03-07T12:00:00Z,INFO,Application started\n")
        file.write("2025-03-07T12:01:00Z,INFO,User logged in\n")
        file.write("2025-03-07T12:02:00Z,ERROR,Database connection failed\n")

# Debugging Information
print("✅ Current Working Directory:", os.getcwd())
print("✅ Files in Directory:", os.listdir())

# Load log data
log_data = pd.read_csv(LOG_FILE)
print("✅ CSV Columns:", log_data.columns.tolist())

# Ensure required columns exist
if 'message' not in log_data.columns:
    raise ValueError("❌ ERROR: Column 'message' is missing in logs.csv!")

if 'loglevel' not in log_data.columns:
    raise ValueError("❌ ERROR: Column 'loglevel' is missing in logs.csv!")

# Convert message column to string
log_data['message'] = log_data['message'].astype(str)

# Encode log messages
encoder = LabelEncoder()
log_data['encoded_message'] = encoder.fit_transform(log_data['message'])

# Prepare training data
X_train = np.array(log_data['encoded_message']).reshape(-1, 1)
y_train = np.array(log_data['loglevel'].apply(lambda x: 1 if x == "ERROR" else 0))

# Build LSTM model
model = Sequential([
    LSTM(50, activation='relu', input_shape=(1,1), return_sequences=True),
    Dropout(0.2),
    LSTM(50, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Ensure the model directory exists before saving
MODEL_DIR = "model"
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

model.save(f"{MODEL_DIR}/log_anomaly_model.h5")
print(f"✅ Model saved to {MODEL_DIR}/log_anomaly_model.h5")

