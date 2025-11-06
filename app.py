import streamlit as st
import numpy as np
import joblib

# Load model & label encoder
model = joblib.load("stress_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="Stress Detection App", layout="centered")

st.title("🧠 Stress Level Prediction App")
st.write("Enter SpO₂ and Heart Rate to predict stress level.")

# User Inputs
spo2 = st.number_input("Enter SpO₂ (%)", min_value=70, max_value=100, value=97)
heartrate = st.number_input("Enter Heart Rate (BPM)", min_value=40, max_value=200, value=90)

# Recommendation function
def recommendation(stress_class):
    if stress_class.lower() == "high stress":
        return "🔴 **High Stress Detected** → Do deep breathing (inhale 4 sec – hold 4 sec – exhale 6 sec), relax, hydrate."
    elif stress_class.lower() == "moderate stress":
        return "🟡 **Moderate Stress** → Take a short walk, stretch, listen to soft music."
    else:
        return "🟢 **Normal Stress Level** → Keep up your healthy routine!"

# Prediction Button
if st.button("Predict Stress Level"):
    features = np.array([[spo2, heartrate]])
    prediction = model.predict(features)[0]
    stress_label = label_encoder.inverse_transform([prediction])[0]

    st.success(f"✅ Predicted Stress: **{stress_label}**")
    st.info(recommendation(stress_label))
