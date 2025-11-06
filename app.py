import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Stress Prediction App", page_icon="💓")

st.title("💓 Stress Type Prediction using SpO₂ & Heart Rate")
st.write("Enter SpO₂ and Heart Rate to predict your stress level.")

col1, col2 = st.columns(2)
spo2 = col1.number_input("SpO₂ (%)", min_value=50, max_value=150, value=98)
hr = col2.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=90)

if st.button("Predict"):
    result = model.predict([[spo2, hr]])[0]

    st.subheader(f"🧠 Stress Type: **{result}**")

    # Stress Reduction Tips
    tips = {
        "Critical Hypoxia": "⚠️ Seek medical help immediately.",
        "High Physiological Stress": "🧘 Deep breathing | Hydrate 💧 | Sit calmly.",
        "Normal / Low Stress": "🎵 Listen to music | Cycling 🚴 | Singing 🎤",
        "Moderate Stress": "🎯 Try dancing 💃 | Walking 🚶 | Yoga 🧘",
        "Severe Stress": "🔥 Do relaxation activities | Swimming 🏊 | Meditation 🧘"
    }

    st.info(tips.get(result, "Stay Healthy!"))
