
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

steps = [
    ("1. Creating dataset", "src/data_preprocessing.py"),
    ("2. Training AI model", "src/train_model.py"),
    ("3. Detecting threats", "src/detect_threats.py"),
    ("4. Generating graphs", "src/visualization.py"),
]

print("=" * 50)
print(" AI-POWERED CYBERSECURITY THREAT DETECTION")
print("=" * 50)

for title, script in steps:
    print(f"\n{'=' * 15} {title} {'=' * 15}")
    result = subprocess.run(
        [sys.executable, str(ROOT / script)],
        cwd=ROOT
    )

    if result.returncode != 0:
        print(f"\nError while running: {script}")
        sys.exit(result.returncode)

print("\nAll project stages completed successfully!")
print("Check the data, models, and outputs folders.")

