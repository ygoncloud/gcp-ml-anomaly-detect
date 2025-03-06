import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import LabelEncoder

# Load log data from Elasticsearch
import os
print("Current Working Directory:", os.getcwd())  # Debugging
print("Files in Directory:", os.listdir())  # Listt All File
with open("logs.csv", "r") as file:
    print("logs.csv content preview:")
    print(file.read())  # Print contents of logs.csv
log_data = pd.read_csv("logs.csv")  # Replace with ELK API query
print("CSV Columns:", log_data.columns.tolist())  # Print available columns
log_data['message'] = log_data['message'].astype(str)

if 'message' not in log_data.columns:
    raise ValueError("❌ ERROR: Column 'message' is missing in logs.csv!")

if 'loglevel' not in log_data.columns:
    raise ValueError("❌ ERROR: Column 'loglevel' is missing in logs.csv!")

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

# Save model
model.save("model/log_anomaly_model.h5")
print("✅ Model saved to model/log_anomaly_model.h5")

