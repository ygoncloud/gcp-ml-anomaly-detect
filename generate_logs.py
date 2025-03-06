import pandas as pd

logs = [
    {"timestamp": "2025-03-06T12:00:00Z", "level": "INFO", "message": "System started"},
    {"timestamp": "2025-03-06T12:05:00Z", "level": "ERROR", "message": "An error occurred"}
]
df = pd.DataFrame(logs)

print("Generated logs:", df)  # Debugging line
df.to_csv("logs.csv", index=False)

