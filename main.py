import streamlit as st
import lightgbm

import pandas as pd
import numpy as np
import joblib


model = joblib.load("pothole_detection_model_pipeline.joblib")

features = [
    'latitude', 'longitude', 'speed',
    'accelerometerX', 'accelerometerY', 'accelerometerZ',
    'gyroX', 'gyroY', 'gyroZ',
    'acclermeter_magnitude', 'gyro_magnitude'
]
st.set_page_config(page_title="Pothole Detector", layout="wide")
st.title("Pothole Detector")
st.markdown("### Predict road potholes using sensor data from accelerometer and gyroscope")
st.subheader("Enter Sensor Readings")
st.markdown("Provide the sensor values below to check if a pothole is detected:")

col1, col2 = st.columns(2)

with col1:
    latitude = st.number_input("Latitude", format="%.6f", help="GPS latitude")
    longitude = st.number_input("Longitude", format="%.6f", help="GPS longitude")
    speed = st.number_input("Speed (m/s)", min_value=0.0, format="%.3f")
    accelerometerX = st.number_input("Accelerometer X", format="%.6f")
    accelerometerY = st.number_input("Accelerometer Y", format="%.6f")

with col2:
    accelerometerZ = st.number_input("Accelerometer Z", format="%.6f")
    gyroX = st.number_input("Gyro X", format="%.6f")
    gyroY = st.number_input("Gyro Y", format="%.6f")
    gyroZ = st.number_input("Gyro Z", format="%.6f")

acclermeter_magnitude = np.sqrt(accelerometerX**2 + accelerometerY**2 + accelerometerZ**2)
gyro_magnitude = np.sqrt(gyroX**2 + gyroY**2 + gyroZ**2)

st.markdown("---")
if st.button("Detect Pothole"):
    input_values = [
        latitude, longitude, speed,
        accelerometerX, accelerometerY, accelerometerZ,
        gyroX, gyroY, gyroZ,
        acclermeter_magnitude, gyro_magnitude
    ]
    if any(pd.isna(v) or v == 0.0 for v in input_values[:3]):  
        st.warning("Please provide valid sensor data (latitude, longitude, and speed are required).")
    else:
        input_df = pd.DataFrame([input_values], columns=features)
        prediction = model.predict(input_df)[0]
        if prediction == 1:
            st.error("⚠️ Pothole Detected! Please slow down and report the location.")
        else:
            st.success("No Pothole Detected. Road seems clear!")
st.markdown("---")
st.caption("Developed with love by @Meenakshi Gupta")
