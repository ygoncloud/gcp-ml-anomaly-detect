import pandas as pd

# Contoh data dummy
data = {"timestamp": ["2024-02-01 12:00", "2024-02-01 12:05"], "event": ["login", "logout"]}
df = pd.DataFrame(data)

# Simpan file logs.csv
df.to_csv("logs.csv", index=False)
print("logs.csv created!")

