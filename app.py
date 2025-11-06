import streamlit as st
import numpy as np
import joblib

# -----------------------------------------
# Load model and encoder
# -----------------------------------------
model = joblib.load("stress_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="Stress Prediction App", layout="centered")
st.title("🧠 Real-Time Stress Monitoring System")
st.write("Enter SpO₂ and Heart Rate to detect stress and receive health suggestions.")

# -----------------------------------------
# Rule-Based analysis (based on medical ranges given by you)
# -----------------------------------------
def evaluate_condition(spo2, hr):
    if spo2 < 60 and hr < 60:
        return "🔴 Critical Hypoxia (Severe Stress)", \
               "⚠ IMMEDIATE MEDICAL ATTENTION REQUIRED.\nCall emergency services."

    elif 60 <= spo2 < 80 and 60 <= hr < 80:
        return "🟠 High Physiological Stress (Hypoxia)", \
               "🚨 Practice deep slow breathing.\n🚨 Sit upright to improve lung function.\n🚨 Seek oxygen support if available."

    elif 80 <= spo2 <= 100 and 80 <= hr <= 100:
        return "🟢 Normal / Low Stress", \
               "✅ You're in a normal state.\n✅ Maintain hydration and continue normal breathing."

    elif 100 < hr <= 120 and 100 <= hr <= 120:
        return "🟡 Moderate Stress / Physical Exertion", \
               "✳ Try grounding yourself.\n✳ Slow breathing: inhale 4s – exhale 6s.\n✳ Take a short walk or stretch."

    elif hr > 120 and spo2 > 120:
        return "🔴 Severe Stress / Hyperactivation", \
               "⚠ Body is in fight-or-flight mode.\n⚠ Sit down, hydrate, avoid stimulation.\n⚠ Take slow deep breaths."

    return "⚠ Out of Range", "Data outside normal physiological sensing range."


# -----------------------------------------
# UI Input fields
# -----------------------------------------
spo2 = st.number_input("Enter SpO₂ (%)", min_value=50, max_value=120, value=97)
heartrate = st.number_input("Enter Heart Rate (BPM)", min_value=40, max_value=200, value=90)

# -----------------------------------------
# Predict button
# -----------------------------------------
if st.button("Predict Stress Level"):
    # ML prediction
    ml_features = np.array([[spo2, heartrate]])
    ml_pred = model.predict(ml_features)[0]
    ml_stress_label = label_encoder.inverse_transform([ml_pred])[0]

    # Rule-based analysis
    condition, health_suggestion = evaluate_condition(spo2, heartrate)

    st.subheader(f"🔍 ML Prediction Result: **{ml_stress_label}**")
    st.subheader(f"📊 Physiological Condition: {condition}")

    st.info(f"💡 Suggested Action:\n{health_suggestion}")
