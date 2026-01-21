import streamlit as st
import pandas as pd
import joblib
import time
from pathlib import Path

# --- Configuration & Styling ---
st.set_page_config(page_title="Star Classifier", page_icon="🌌", layout="centered")

# --- Optimized Functions ---
@st.cache_resource
def load_model():
    # FIX: Points to the 'model' subfolder where model.pkl is located
    model_path = Path(__file__).parent / "model" / "model.pkl"
    
    if not model_path.exists():
        st.error(f"❌ Model file not found at: {model_path}")
        st.stop()
        
    return joblib.load(model_path)

def wrangle_input(u, g, r, i, z):
    """Computes color features and returns a formatted DataFrame"""
    data = {
        "u": u, "g": g, "r": r, "i": i, "z": z,
        "u_g": u - g,
        "g_r": g - r,
        "r_i": r - i,
        "i_z": i - z
    }
    return pd.DataFrame([data])

# --- UI Layout ---
st.title("Astronomical Object Classifier 🌌")
st.markdown("Predict whether a celestial body is a **Galaxy**, **Quasar (QSO)**, or a **Star**.")

st.subheader("Input Magnitudes (Typical Range: 14–25)")
col1, col2, col3 = st.columns(3)

with col1:
    u = st.number_input("u band (Ultraviolet)", min_value=14.0, max_value=25.0, value=14.0, step=0.1)
    g = st.number_input("g band (Green)", min_value=14.0, max_value=25.0, value=14.0, step=0.1)
with col2:
    r = st.number_input("r band (Red)", min_value=14.0, max_value=25.0, value=14.0, step=0.1)
    i = st.number_input("i band (Near IR)", min_value=14.0, max_value=25.0, value=14.0, step=0.1)
with col3:
    z = st.number_input("z band (Infrared)", min_value=14.0, max_value=25.0, value=14.0, step=0.1)

st.divider()

# --- Prediction Logic ---
label_map = {0: "GALAXY 🌀", 1: "QSO (QUASAR) 💎", 2: "STAR ⭐"}

# Define acceptable intervals
intervals = {
    "u": (14, 25),
    "g": (14, 25),
    "r": (14, 25),
    "i": (14, 25),
    "z": (14, 25)
}

if st.button("Analyze Object", type="primary", use_container_width=True):
    # Check if inputs are within allowed ranges
    out_of_range = []
    for band, (low, high) in intervals.items():
        value = locals()[band]
        if not (low <= value <= high):
            out_of_range.append(f"{band} ({low}-{high})")

    if out_of_range:
        st.error(f"❌ The following inputs are out of range: {', '.join(out_of_range)}. Prediction not allowed.")
    else:
        with st.status("Running classification...", expanded=True) as status:
            st.write("Loading model...")
            model = load_model()

            st.write("Processing features...")
            X_input = wrangle_input(u, g, r, i, z)
            time.sleep(0.3)

            st.write("Predicting...")
            numeric_pred = model.predict(X_input)[0]
            pred_label = label_map.get(numeric_pred, "Unknown")

            status.update(label="Analysis Complete!", state="complete", expanded=False)

        st.balloons()
        st.markdown(f"### Result: **{pred_label}**")

        if hasattr(model, "predict_proba"):
            proba = float(model.predict_proba(X_input).max())
            st.write(f"Confidence: **{proba * 100:.1f}%**")
            st.progress(proba)
