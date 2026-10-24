# AI-Powered Cybersecurity Threat Detection System

## Project Overview
This project uses a Machine Learning model to classify network traffic as Normal or Suspicious. It demonstrates how AI can help identify potentially suspicious network activity.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib
- Joblib

## Features
- Synthetic network traffic dataset generation
- Data preprocessing
- Random Forest classification model
- Model evaluation using accuracy, precision, recall, and F1-score
- Detection of normal and suspicious network records
- Visualizations of model results and feature importance

## Project Structure
- `data/` – Generated network traffic dataset
- `models/` – Saved trained model
- `outputs/` – Generated graphs
- `src/` – Python source code
- `main.py` – Project entry point
- `requirements.txt` – Required Python libraries

## How to Run
Run these commands in the VS Code terminal from the project folder:

```bash
python src/data_preprocessing.py
python src/train_model.py
python src/detect_threats.py
python src/visualization.py
```

## Important Note
This prototype uses a **synthetic dataset** for demonstration and learning. Its results do not establish real-world cybersecurity detection performance. Testing on a suitable public network-security dataset is needed for real-world evaluation.
