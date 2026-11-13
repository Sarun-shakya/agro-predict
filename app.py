import streamlit as st
import joblib
import pandas as pd
import os

crop_images = {
    'rice': 'images/rice.png',
    'maize': 'images/maize.png',
    'chickpea': 'images/chickpea.png',
    'kidneybeans': 'images/kidneybeans.png',
    'pigeonpeas': 'images/pigeonpeas.png',
    'mothbeans': 'images/mothbeans.png',
    'mungbean': 'images/mungbean.png',
    'blackgram': 'images/blackgram.png',
    'lentil': 'images/lentil.png',
    'pomegranate': 'images/pomegranate.png',
    'banana': 'images/banana.png',
    'mango': 'images/mango.png',
    'grapes': 'images/grapes.png',
    'watermelon': 'images/watermelon.png',
    'muskmelon': 'images/muskmelon.png',
    'apple': 'images/apple.png',
    'orange': 'images/orange.png',
    'papaya': 'images/papaya.png',
    'coconut': 'images/coconut.png',
    'cotton': 'images/cotton.png',
    'jute': 'images/jute.png',
    'coffee': 'images/coffee.png'
}

# Load trained model
model = joblib.load("crop_model.pkl")

# Page configuration
st.set_page_config(
    page_title="AgroPredict",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 AgroPredict")
st.write(
    "Enter the soil and environmental conditions "
    "to get a suitable crop recommendation."
)

st.divider()

# Input fields
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", 0, 140, 90)
    P = st.number_input("Phosphorus (P)", 0, 145, 42)
    K = st.number_input("Potassium (K)", 0, 205, 43)
    temperature = st.number_input(
        "Temperature (°C)", 0.0, 50.0, 20.8
    )

with col2:
    humidity = st.number_input(
        "Humidity (%)", 0.0, 100.0, 82.0
    )
    ph = st.number_input(
        "Soil pH", 0.0, 14.0, 6.5
    )
    rainfall = st.number_input(
        "Rainfall (mm)", 0.0, 400.0, 202.0
    )

st.divider()

# Prediction
if st.button("Recommend Crop 🌾", use_container_width=True):

    input_data = pd.DataFrame([{
        'N': N,
        'P': P,
        'K': K,
        'temperature': temperature,
        'humidity': humidity,
        'ph': ph,
        'rainfall': rainfall
    }])

    prediction = model.predict(input_data)[0]

    st.success("Crop Recommendation Generated!")

    st.subheader(f"🌱 Recommended Crop: {prediction.capitalize()}")

    image_path = crop_images.get(prediction.lower())

    if image_path and os.path.exists(image_path):
        st.image(
            image_path,
            caption=prediction.capitalize(),
            use_container_width=True
        )
    else:
        st.warning("Crop image not found.")
