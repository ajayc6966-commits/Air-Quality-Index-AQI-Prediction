import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.title("🌍 Universal AQI Predictor")
st.write("Enter pollutant levels of ANY city (Google the current values for Indore, etc.)")

# Inputs
pm25 = st.number_input("PM2.5 Level", value=50.0)
no2 = st.number_input("NO2 Level", value=25.0)
co = st.number_input("CO Level", value=1.0)
so2 = st.number_input("SO2 Level", value=10.0)
o3 = st.number_input("Ozone Level", value=30.0)

if st.button("Predict Now"):
    # Ab humein city encoder ki zaroorat nahi
    features = np.array([[pm25, no2, co, so2, o3]])
    prediction = model.predict(features)[0]
    
    st.header(f"Predicted AQI: {int(prediction)}")
    
    if prediction <= 50: st.success("Good ✅")
    elif prediction <= 100: st.info("Satisfactory 🙂")
    elif prediction <= 200: st.warning("Moderate ⚠️")
    else: st.error("Poor/Hazardous 💀")