import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from generator import generate_synthetic_data
from drift import calculate_drift
from security import detect_pii

# Page config
st.set_page_config(
    page_title="AI Synthetic Data System",
    page_icon="🔐",
    layout="wide"
)

# Header
st.title("🔐 AI Synthetic Data & Security Dashboard")
st.markdown("### 🚀 Privacy-Preserving Data Generator with Drift & Cyber Intelligence")
st.markdown("---")

# Upload
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Original Data")
        st.write(data.head())

    with col2:
        st.subheader("🔐 PII Detection")
        pii_results = detect_pii(data)
        st.write(pii_results)

    # Generate button
    if st.button("🚀 Generate Synthetic Data"):
        with st.spinner("Generating synthetic data..."):
            synthetic = generate_synthetic_data(data)

        # Show synthetic data
        st.subheader("🤖 Synthetic Data")
        st.write(synthetic.head())

        # Drift calculation
        drift = calculate_drift(data, synthetic)

        st.subheader("📉 Drift Scores")

        high_drift_cols = []

        for col, value in drift.items():
            if value > 1:
                st.error(f"🚨 High Drift in {col}: {value}")
                high_drift_cols.append(col)
            elif value > 0.5:
                st.warning(f"⚠️ Moderate Drift in {col}: {value}")
            else:
                st.success(f"✅ Low Drift in {col}: {value}")

        # Summary Metrics
        st.subheader("📌 Summary Metrics")

        m1, m2, m3 = st.columns(3)
        m1.metric("Rows", len(data))
        m2.metric("Columns", len(data.columns))
        m3.metric("High Drift Columns", len(high_drift_cols))

        # Global Alert
        if high_drift_cols:
            st.error(f"🚨 Critical Drift Detected in: {', '.join(high_drift_cols)}")
        else:
            st.success("✅ No Critical Drift Detected")

        # Graphs
        st.subheader("📊 Data Distribution Comparison")

        for col in data.columns:
            if data[col].dtype != 'object':
                fig, ax = plt.subplots()

                ax.hist(data[col], bins=20, alpha=0.5, label='Real')
                ax.hist(synthetic[col], bins=20, alpha=0.5, label='Synthetic')

                ax.set_title(f"{col} Distribution")
                ax.legend()

                st.pyplot(fig)