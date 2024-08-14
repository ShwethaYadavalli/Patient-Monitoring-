import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Simulate real-time patient data (e.g., heart rate)
def generate_patient_data(num_samples=100):
    np.random.seed(42)
    time = pd.date_range(start='2023-01-01', periods=num_samples, freq='T')  # Data for every minute
    heart_rate = np.random.normal(70, 5, num_samples)
    heart_rate[90:95] = heart_rate[90:95] + np.random.normal(15, 2, 5)  # Injecting anomalies
    return pd.DataFrame({'Time': time, 'HeartRate': heart_rate})

# Anomaly detection using Isolation Forest
def detect_anomalies(df):
    model = IsolationForest(contamination=0.05)  # Adjust contamination to expected anomaly rate
    df['Anomaly'] = model.fit_predict(df[['HeartRate']])
    df['Anomaly'] = df['Anomaly'].apply(lambda x: 1 if x == -1 else 0)
    return df

# Predictive analytics: Simple moving average
def moving_average(df, window=5):
    df['HeartRate_MA'] = df['HeartRate'].rolling(window=window).mean()
    return df

# Streamlit dashboard
st.title("Real-Time Patient Monitoring System")

# Generate patient data
data = generate_patient_data()

# Anomaly detection
data = detect_anomalies(data)

# Predictive analytics
data = moving_average(data)

# Display data
st.write("### Patient Data Overview")
st.write(data)

# Plot the data
st.write("### Heart Rate Over Time")
fig, ax = plt.subplots()
ax.plot(data['Time'], data['HeartRate'], label='Heart Rate')
ax.plot(data['Time'], data['HeartRate_MA'], label='Moving Average', linestyle='--')
anomalies = data[data['Anomaly'] == 1]
ax.scatter(anomalies['Time'], anomalies['HeartRate'], color='red', label='Anomaly', zorder=5)
ax.legend()
st.pyplot(fig)

# Highlight anomalies
st.write("### Anomalies Detected")
st.write(anomalies)
