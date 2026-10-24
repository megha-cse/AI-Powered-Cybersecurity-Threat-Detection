import joblib
import pandas as pd

from pathlib import Path

# Locate the saved model
ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "cybersecurity_model.pkl"

# Load the trained AI model
model = joblib.load(MODEL_PATH)

# Sample network records to analyze
test_data = pd.DataFrame([
    {
        "packet_size": 500,
        "failed_logins": 0,
        "request_frequency": 10,
        "bytes_sent": 5000,
        "connection_duration": 120
    },
    {
        "packet_size": 1400,
        "failed_logins": 10,
        "request_frequency": 200,
        "bytes_sent": 80000,
        "connection_duration": 5
    }
])

# Predict whether each record is suspicious
predictions = model.predict(test_data)
probabilities = model.predict_proba(test_data)

print("\n===== CYBERSECURITY THREAT DETECTION =====")

for i, prediction in enumerate(predictions):
    status = "SUSPICIOUS ACTIVITY" if prediction == 1 else "NORMAL ACTIVITY"

    print(f"\nNetwork Record {i + 1}")
    print("-" * 35)
    print(test_data.iloc[i].to_dict())
    print("Prediction:", status)
    print(f"Model confidence: {probabilities[i][prediction] * 100:.2f}%")

    if prediction == 1:
        print("ALERT: Investigate this record!")
    else:
        print("No alert generated.")

print("\nDetection test completed!")