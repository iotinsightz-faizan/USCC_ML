from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load model and label encoder
model = joblib.load("stress_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

def stress_recommendation(stress_class):
    if stress_class.lower() == "high stress":
        return "🔴 HIGH STRESS: Take deep breathing (inhale 4 sec – hold 4 sec – exhale 6 sec), sit calm, drink water."
    elif stress_class.lower() == "moderate stress":
        return "🟡 MODERATE STRESS: Take a 3-minute walk, stretch your shoulders, listen to calm music."
    elif stress_class.lower() == "normal":
        return "🟢 NORMAL: Stress level is fine. Maintain hydration and continue your routine."
    else:
        return "⚠ No recommendation available."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    spo2 = float(request.form["spo2"])
    hr = float(request.form["heartrate"])

    # Model input preparation
    features = np.array([[spo2, hr]])
    prediction = model.predict(features)[0]

    stress_label = label_encoder.inverse_transform([prediction])[0]
    recommendation = stress_recommendation(stress_label)

    return render_template("index.html",
                           result=f"Predicted Stress: {stress_label}",
                           recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)
