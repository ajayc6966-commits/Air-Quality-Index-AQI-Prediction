🌍 Air Quality Index (AQI) Predictor
📌 Project Overview
This project is a Machine Learning-based Web Application designed to predict the Air Quality Index (AQI) of any city based on major atmospheric pollutants. Clean air is essential for health, and this tool helps users monitor environmental safety by providing real-time predictions using historical data patterns.

🚀 How it Works
The application uses a Random Forest Regressor model trained on the city_day.csv dataset (a comprehensive Indian air quality dataset). Users can input levels of specific pollutants, and the model calculates the expected AQI value, categorizing it from "Good" to "Hazardous."

📊 Key Features
Universal Prediction: Unlike models restricted to specific cities, this tool uses chemical concentrations to predict AQI for any location (e.g., Indore, Delhi, etc.).

Real-time Inputs: Interactive sliders/number inputs for pollutants like PM2.5, NO2, CO, SO2, and Ozone.

User-Friendly Interface: Built with Streamlit for a clean and responsive web experience.

Instant Feedback: Categorizes air quality into standard health safety zones (Good, Satisfactory, Moderate, Poor, Hazardous).

🛠️ Tech Stack
Language: Python

Libraries: Pandas, Scikit-learn, NumPy

Web Framework: Streamlit

Model: Random Forest Regression
