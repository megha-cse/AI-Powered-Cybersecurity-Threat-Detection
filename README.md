🛡️ AI-Powered Cybersecurity Threat Detection System

Overview

CyberShield AI is a machine-learning-based cybersecurity demonstration project that analyzes network traffic features and classifies records as Normal or Suspicious.

Features

* Synthetic network traffic dataset generation
* Random Forest classification model
* Suspicious activity prediction
* Model confidence display
* Confusion matrix visualization
* Feature importance analysis
* Interactive Streamlit dashboard

Technologies Used

* Python
* Pandas and NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Git and GitHub

Project Structure

AI-Powered Cybersecurity Threat Detection/
├── data/
├── models/
├── outputs/
├── src/
│   ├── data_preprocessing.py
│   ├── train_model.py
│   ├── detect_threats.py
│   └── visualization.py
├── app.py
├── main.py
└── requirements.txt

How to Run

1. Install the required packages:
    pip install -r requirements.txt
2. Generate the dataset:
    python src/data_preprocessing.py
3. Train the model:
    python src/train_model.py
4. Generate visualizations:
    python src/visualization.py
5. Launch the dashboard:
    python -m streamlit run app.py

Dataset Disclaimer

This project currently uses synthetically generated network traffic data for demonstration and educational purposes. Its results do not establish real-world cybersecurity detection performance.

Future Improvements

* Train and evaluate using a suitable public cybersecurity dataset
* Improve model validation and threat detection
* Add more traffic features and threat categories
* Explore real-time monitoring with appropriate network data

Author

Megha
📸 Dashboard Screenshots

1. CyberShield AI Dashboard

2. Normal Traffic Detection

3. Suspicious Traffic Detection