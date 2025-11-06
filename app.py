import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Stress Detection App", layout="centered")

st.title("💓 Stress Level Prediction using Heart Rate & SpO₂")
st.write("Enter your Heart Rate and SpO₂ to predict the type of stress.")

# User inputs
spo2 = st.number_input("SpO₂ Level (%)", min_value=50, max_value=150, value=98)
hr = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=90)

if st.button("Predict Stress"):
    result = model.predict([[spo2, hr]])[0]

    st.subheader(f"Stress Type: **{result}**")

    st.write("💡 Tips to reduce stress:")

    if result == "Critical Hypoxia":
        st.error("⚠️ Seek medical help immediately.")

    elif result == "Severe Stress":
        st.warning("🚨 Take deep breaths, drink water, relax.")
        st.write("- Dancing 💃\n- Swimming 🏊\n- Singing 🎤")

    elif result == "Moderate Stress":
        st.info("😌 Try relaxation activities:")
        st.write("- Walking 🚶\n- Slow breathing 🧘\n- Light exercise 🏃")

    elif result == "High Physiological Stress":
        st.info("🫁 Oxygen level low — relax your body.")
        st.write("- Sit calmly 🧘\n- Hydrate 💧")

    else:
        st.success("✅ You are relaxed. Maintain healthy habits!")
        st.write("- Music 🎶\n- Cycling 🚴\n- Meditation 🧘")
