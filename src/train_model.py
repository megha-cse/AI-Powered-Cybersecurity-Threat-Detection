import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Locate project folders
ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "network_traffic.csv"
MODEL_PATH = ROOT / "models" / "cybersecurity_model.pkl"

# Load the dataset
data = pd.read_csv(DATA_PATH)

print("Dataset loaded:", data.shape)

# Separate input features and target label
X = data.drop(columns=["label"])
y = data["label"]

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create and train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

print("\nTraining AI model...")
model.fit(X_train, y_train)

# Predict on unseen test records
predictions = model.predict(X_test)

# Evaluate the model
print("\n--- Model Evaluation ---")
print(f"Accuracy:  {accuracy_score(y_test, predictions):.4f}")
print(f"Precision: {precision_score(y_test, predictions, zero_division=0):.4f}")
print(f"Recall:    {recall_score(y_test, predictions, zero_division=0):.4f}")
print(f"F1 Score:  {f1_score(y_test, predictions, zero_division=0):.4f}")

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    target_names=["Normal", "Suspicious"],
    zero_division=0
))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Save the trained model
joblib.dump(model, MODEL_PATH)

print(f"\nTrained model saved to: {MODEL_PATH}")
print("Model training completed successfully!")