# Project_3
Trip Fare : Predicting Urban Taxi Fare with Machine Learning

# Taxi Fare Prediction 🚚

This mini-project is a web application for predicting NYC taxi fares based on pickup/dropoff coordinates, passenger count, and trip time. It uses a trained ML model and runs entirely on Google Colab using Streamlit + ngrok, so no local setup is required.

---

## 🚀 Project Structure

```
├── regression.ipynb            # Script for cleaning, feature engineering, and training
├── taxi_fare_predictor.pkl     # Saved trained model 
├── taxi_streamlit.ipynb        # Streamlit UI for live predictions
├── taxi_data.csv               # NYC taxi trip dataset
└── README.md                   # Project documentation
```

---

## 📊 Dataset

`taxi_data.csv` contains historical NYC taxi trip data:

* Pickup/Dropoff coordinates
* Passenger count
* Fare details (tip, tax, etc.)
* Datetime & vendor info

---
## 📦 Features
* Estimate fare based on trip distance and time

* User-friendly web UI with Streamlit

* Hosted from Colab via public ngrok link

* Supports .pkl models trained with scikit-learn, xgboost, and pandas

---
## 💻 Streamlit App 

## 🧪 How to Run in Google Colab
* Open the Colab notebook.

* Run each cell step-by-step:

* Install dependencies

* Upload your trained model (taxi_fare_predictor.pkl)

* Auto-generate the app.py file (Streamlit code)

* Launch app with ngrok (public link appears)

* Click the ngrok link printed in the final cell to access your live app.

## 💡 Inputs in the App
* Pickup Date and Time

* Pickup Latitude & Longitude

* Dropoff Latitude & Longitude

* Passenger Count

## 📈 Output
* Predicted Fare in USD based on the input trip

## 🔧 Dependencies
Ensure the following versions were used to train your model (for compatibility):

```bash
scikit-learn==1.6.1  
xgboost==3.0.3  
pandas==2.2.2  
streamlit  
pyngrok  
cloudpickle  
```
---



