import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model and expected feature columns
model = joblib.load('best_fare_model.pkl')
expected_features = joblib.load('best_fare_model_features.pkl')

# Streamlit UI
st.title("🚖 Taxi Fare Predictor")
import streamlit as st

st.header("Enter Trip Details")
pickup_longitude = st.number_input("Pickup Longitude", value=-73.98)
pickup_latitude = st.number_input("Pickup Latitude", value=40.76)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-74.00)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.75)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=1)
store_and_fwd_flag = st.selectbox("Store and Forward Flag", options=[0, 1])  # Assuming encoded

# Background image using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMtz5PF0KrwvxW4_ZdxzhJRqSsdZ1EFn_45w&s);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add any other inputs as per your training features...

if st.button("Predict Fare"):
    # Collect inputs into a single-row DataFrame
    input_dict = {
        'pickup_longitude': [pickup_longitude],
        'pickup_latitude': [pickup_latitude],
        'dropoff_longitude': [dropoff_longitude],
        'dropoff_latitude': [dropoff_latitude],
        'passenger_count': [passenger_count],
        'store_and_fwd_flag': [store_and_fwd_flag],
        # Add other fields here as needed
    }

    input_df = pd.DataFrame(input_dict)

    # === FIX FEATURE MISMATCH ===
    for col in expected_features:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[expected_features]  # Reorder to match model

    # Predict
    fare = model.predict(input_df)[0]
    st.success(f"💰 Predicted Total Fare: ${fare:.2f}")
