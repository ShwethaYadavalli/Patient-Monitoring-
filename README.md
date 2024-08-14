# Patient-Monitoring-
Patient Monitoring System with Anomaly Detection & Predictive Analytics

## Objective:
Create a web-based dashboard where you can see the real-time patient monitoring data, detect anomalies, and observe the moving average of the heart rate.

## Explanation of the code:
### Data Simulation
The *generate_patient_data()* function simulates heart rate data for a patient, with some anomalies injected to test the detection system.
### Anomaly Detection
The *detect_anomalies()* function uses an IsolationForest model to detect anomalies in the heart rate data. Points classified as anomalies are labeled with a 1. 
#### Threshold sliders
Allow users to dynamically adjust the anomaly detection thresholds and see how it impacts the results. Default threshold is 0.05.
### Predictive Analytics
The *moving_average()* function calculates a simple moving average of the heart rate, which can be used to predict future trends or smooth out short-term fluctuations.
### Streamlit Dashboard
The Streamlit app visualizes the heart rate data, highlights detected anomalies, and shows the moving average. It also allows for the simulation of live data updates with the press of a button.
