# Project_3
Trip Fare : Predicting Urban Taxi Fare with Machine Learning

# Taxi Fare Prediction 🚚

This project predicts the total fare amount for taxi trips using a machine learning model. It includes data preprocessing, model training with Random Forest, hyperparameter tuning, and a deployed Streamlit app for real-time fare predictions.

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

## 🧑‍💻 Model

* **Algorithm:** Random Forest Regressor
* **Evaluation Metric:** RMSE
* **Tuning:** RandomizedSearchCV
* **Best Params:** Automatically selected and stored

---

## 💻 Streamlit App (`fare_prediction.py`)

**What it does:**

* Accepts inputs like location, time, passenger count, etc.
* Displays predicted total fare from trained model

### To Run:

```bash
streamlit run fare_prediction.py
```

---

## ✅ Setup Instructions

1. **Create Environment:**

```bash
python -m venv myenv
myenv\Scripts\activate  # Windows
```

2. **Install Requirements:**

```bash
pip install -r requirements.txt
# or install manually:
pip install pandas scikit-learn streamlit matplotlib seaborn
```

---

## 🔧 Notes

* Python 3.11 was used
* Ensure column alignment between training and prediction features
* Streamlit UI includes background image and trip duration

---

Happy Predicting! 🤝
