import pandas as pd
import joblib
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay

# Find project folders
ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "network_traffic.csv"
MODEL_PATH = ROOT / "models" / "cybersecurity_model.pkl"
OUTPUT_PATH = ROOT / "outputs"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# Load dataset and trained model
data = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)

X = data.drop(columns=["label"])
y = data["label"]

# Use the same test split as training
_, X_test, _, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

predictions = model.predict(X_test)

# 1. Confusion matrix
ConfusionMatrixDisplay.from_predictions(
    y_test,
    predictions,
    display_labels=["Normal", "Suspicious"],
    cmap="Blues"
)
plt.title("Cybersecurity Detection - Confusion Matrix")
plt.tight_layout()
plt.savefig(OUTPUT_PATH / "confusion_matrix.png", dpi=150)
plt.close()

# 2. Dataset class distribution
counts = data["label"].map({
    0: "Normal",
    1: "Suspicious"
}).value_counts()

counts.plot(kind="bar", rot=0)
plt.title("Network Records by Class")
plt.xlabel("Traffic Class")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig(OUTPUT_PATH / "traffic_distribution.png", dpi=150)
plt.close()

# 3. Feature importance
importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values()

importance.plot(kind="barh")
plt.title("Model Feature Importance")
plt.xlabel("Importance")
plt.tight_layout()
plt.savefig(OUTPUT_PATH / "feature_importance.png", dpi=150)
plt.close()

print("Visualization completed successfully!")
print("Saved graphs:")
print(OUTPUT_PATH / "confusion_matrix.png")
print(OUTPUT_PATH / "traffic_distribution.png")
print(OUTPUT_PATH / "feature_importance.png")
