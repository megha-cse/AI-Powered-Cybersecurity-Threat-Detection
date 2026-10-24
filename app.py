import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ---------- PROJECT PATHS ----------
ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "cybersecurity_model.pkl"
DATA_PATH = ROOT / "data" / "network_traffic.csv"
OUTPUT_PATH = ROOT / "outputs"

# ---------- PAGE CONFIGURATION ----------
st.set_page_config(
    page_title="CyberShield AI",
    page_icon="🛡️",
    layout="wide"
)

# ---------- CUSTOM STYLE ----------
st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: #e5e7eb;
}
[data-testid="stSidebar"] {
    background-color: #111827;
}
div[data-testid="stMetric"] {
    background-color: #172033;
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 12px;
}
.stButton > button {
    width: 100%;
    border-radius: 8px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD MODEL ----------
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

st.sidebar.title("🛡️ CyberShield AI")
st.sidebar.caption("Machine Learning Security Dashboard")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Threat Detection", "Model Insights"]
)

st.sidebar.divider()
st.sidebar.info("Demo mode: using a synthetic network traffic dataset.")

if not MODEL_PATH.exists():
    st.error("Trained model not found. Run: python main.py")
    st.stop()

if not DATA_PATH.exists():
    st.error("Dataset not found. Run: python main.py")
    st.stop()

model = load_model()
data = load_data()

# ---------- DASHBOARD PAGE ----------
if page == "Dashboard":
    st.title("🛡️ CyberShield AI")
    st.subheader("AI-Powered Cybersecurity Threat Detection")
    st.write(
        "Monitor sample network traffic and identify "
        "potentially suspicious activity using machine learning."
    )

    total_records = len(data)
    suspicious_records = int((data["label"] == 1).sum())
    normal_records = int((data["label"] == 0).sum())

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Records", f"{total_records:,}")
    c2.metric("Normal Records", f"{normal_records:,}")
    c3.metric("Suspicious Records", f"{suspicious_records:,}")

    st.divider()
    st.subheader("📊 Network Traffic Distribution")

    counts = (
        data["label"]
        .map({0: "Normal", 1: "Suspicious"})
        .value_counts()
    )
    st.bar_chart(counts)

    st.caption(
        "These counts represent the generated demonstration dataset, "
        "not live network traffic."
    )

    st.subheader("🔎 Recent Sample Records")
    st.dataframe(data.tail(10), use_container_width=True)

# ---------- THREAT DETECTION PAGE ----------
elif page == "Threat Detection":
    st.title("🔍 Network Threat Detection")
    st.write(
        "Enter network traffic characteristics and let the trained "
        "Random Forest model classify the record."
    )

    with st.form("threat_form"):
        st.subheader("Network Traffic Details")

        c1, c2 = st.columns(2)

        with c1:
            packet_size = st.number_input(
                "Packet Size (bytes)",
                min_value=1,
                max_value=1000000,
                value=500
            )
            failed_logins = st.number_input(
                "Failed Login Attempts",
                min_value=0,
                max_value=10000,
                value=0
            )
            request_frequency = st.number_input(
                "Request Frequency",
                min_value=0,
                max_value=100000,
                value=10
            )

        with c2:
            bytes_sent = st.number_input(
                "Bytes Sent",
                min_value=0,
                max_value=100000000,
                value=5000
            )
            connection_duration = st.number_input(
                "Connection Duration (seconds)",
                min_value=0,
                max_value=1000000,
                value=120
            )

        submitted = st.form_submit_button(
            "🔍 Analyze Network Traffic",
            type="primary"
        )

    if submitted:
        record = pd.DataFrame([{
            "packet_size": packet_size,
            "failed_logins": failed_logins,
            "request_frequency": request_frequency,
            "bytes_sent": bytes_sent,
            "connection_duration": connection_duration
        }])

        prediction = int(model.predict(record)[0])
        probabilities = model.predict_proba(record)[0]
        confidence = float(probabilities[prediction]) * 100

        st.divider()
        st.subheader("Analysis Result")

        if prediction == 1:
            st.error("🚨 SUSPICIOUS ACTIVITY DETECTED")
            st.warning(
                "Review this record before taking action. "
                "This prediction alone does not prove an attack."
            )
        else:
            st.success("✅ CLASSIFIED AS NORMAL ACTIVITY")
            st.info(
                "The model classified this record as normal. "
                "This does not guarantee that the traffic is safe."
            )

        a, b = st.columns(2)
        a.metric("Model Confidence", f"{confidence:.2f}%")
        b.metric(
            "Predicted Class",
            "Suspicious" if prediction == 1 else "Normal"
        )

        st.progress(int(round(confidence)))
        st.caption(
            "Confidence is the model's estimated class probability, "
            "not a guarantee of real-world correctness."
        )

        with st.expander("View analyzed input"):
            st.dataframe(record, use_container_width=True)

# ---------- MODEL INSIGHTS PAGE ----------
elif page == "Model Insights":
    st.title("📈 Model Insights")
    st.write("Explore the model's input features and generated graphs.")

    importance = pd.Series(
        model.feature_importances_,
        index=model.feature_names_in_
    ).sort_values(ascending=False)

    st.subheader("Feature Importance")
    st.bar_chart(importance)

    st.caption(
        "Feature importance shows how the trained model used its inputs. "
        "It does not establish causation."
    )

    graph_files = [
        ("Confusion Matrix", "confusion_matrix.png"),
        ("Traffic Distribution", "traffic_distribution.png"),
        ("Feature Importance Graph", "feature_importance.png")
    ]

    for title, filename in graph_files:
        graph_path = OUTPUT_PATH / filename
        if graph_path.exists():
            st.subheader(title)
            st.image(str(graph_path), use_container_width=True)

    st.subheader("Dataset Information")
    st.write(f"Records: {len(data):,}")
    st.write(f"Input features: {len(model.feature_names_in_)}")
    st.write("Algorithm: Random Forest Classifier")
    st.write("Dataset type: Synthetic / generated for demonstration")

    st.warning(
        "Educational prototype only. The dataset is synthetic and "
        "does not validate performance against real cyberattacks. "
        "Use a suitable public security dataset for realistic evaluation."
    )

# ---------- FOOTER ----------
st.divider()
st.caption(
    "CyberShield AI | Educational cybersecurity prototype | "
    "No live network monitoring is performed."
)