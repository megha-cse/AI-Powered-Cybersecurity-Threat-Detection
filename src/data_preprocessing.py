import pandas as pd
import numpy as np
from pathlib import Path

# Make the results reproducible
np.random.seed(42)

# Number of simulated network records
n = 2000

# Generate normal network activity
normal = pd.DataFrame({
    "packet_size": np.random.randint(100, 1200, n),
    "failed_logins": np.random.poisson(0.2, n),
    "request_frequency": np.random.randint(1, 40, n),
    "bytes_sent": np.random.randint(500, 15000, n),
    "connection_duration": np.random.randint(5, 300, n),
    "label": 0
})

# Generate simulated suspicious activity
attack = pd.DataFrame({
    "packet_size": np.random.randint(700, 1501, n),
    "failed_logins": np.random.randint(3, 15, n),
    "request_frequency": np.random.randint(60, 301, n),
    "bytes_sent": np.random.randint(15000, 100001, n),
    "connection_duration": np.random.randint(1, 30, n),
    "label": 1
})

# Combine normal and suspicious records
data = pd.concat([normal, attack], ignore_index=True)

# Shuffle the records
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Find the project root directory
project_root = Path(__file__).resolve().parent.parent
output_file = project_root / "data" / "network_traffic.csv"

# Save the dataset
data.to_csv(output_file, index=False)

print("Cybersecurity dataset created successfully!")
print(f"Dataset location: {output_file}")
print(f"Total records: {len(data)}")
print("\nFirst five records:")
print(data.head())

print("\nClass distribution:")
print(data["label"].value_counts().rename(
    index={0: "Normal", 1: "Suspicious"}
))