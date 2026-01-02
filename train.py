import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Data Load
df = pd.read_csv('city_day.csv')

# Sirf Pollutants le rahe hain (City hata di hai)
cols = ['PM2.5', 'NO2', 'CO', 'SO2', 'O3', 'AQI']
df = df[cols].dropna()

X = df[['PM2.5', 'NO2', 'CO', 'SO2', 'O3']]
y = df['AQI']

# Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X.values, y)

# Save Model
pickle.dump(model, open('model.pkl', 'wb'))
print("✅ Universal Model Taiyar hai!")