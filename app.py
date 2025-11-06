import streamlit as st
import numpy as np
import joblib

# Load model and encoder
model = joblib.load("stress_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="Stress Monitoring System", layout="centered")

st.title("🧠 Stress Level Prediction System")
st.write("Enter SpO₂ and Heart Rate to predict stress level and get suggestions to reduce stress.")

# -----------------------------
# Stress Reduction Suggestions
# -----------------------------
def suggestion(stress_class):
    stress_class = stress_class.lower()

    if stress_class == "high stress":
        return """
        ✅ Try these activities to reduce stress:
        - Deep Breathing (4s inhale – 4s hold – 6s exhale)
        - Dancing for 5-10 minutes
        - Cycling / Riding to change mood
        - Swimming to relax body & improve O₂ flow
        - Listen to slow calming music
        """

    elif stress_class == "moderate stress":
        return """
        ✅ You're experiencing moderate stress. Try:
        - Short walk for fresh air
        - Light stretching or yoga
        - Talk with friends / take a break
        - Hobby time: Drawing, Playing games
        """

    elif stress_class == "normal":
        return """
        ✅ Your stress level is normal.
        - Keep enjoying your routine
        - Maintain hydration
        - Continue healthy lifestyle
        """

    else:
        return "⚠ Unable to determine stress level."

# -----------------------------
# User Inputs
# -----------------------------
spo2 = st.number_input("Enter SpO₂ (%)", min_value=40, max_value=100, value=97)
heartrate = st.number_input("Enter Heart Rate (BPM)", min_value=40, max_value=200, value=90)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Stress Level"):
    input_values = np.array([[spo2, heartrate]])
    prediction = model.predict(input_values)[0]
    stress_label = label_encoder.inverse_transform([prediction])[0]

    st.subheader(f"🔍 ML Prediction Result: **{stress_label}**")
    st.info(suggestion(stress_label))
