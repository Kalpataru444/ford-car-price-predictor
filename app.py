import streamlit as st
import pandas as pd
import joblib

# Load the trained ML pipeline
model = joblib.load("car_price_model.pkl")

st.set_page_config(
    page_title="Ford Car Price Predictor",
    page_icon="🚗"
)

st.title("🚗 Ford Car Price Predictor")
st.write("Enter the details of a Ford vehicle to estimate its resale price.")

# Categorical options
car_models = [
    ' Grand C-MAX', ' Fiesta', ' Focus', ' Edge', ' C-MAX',
    ' Ka+', ' KA', ' Kuga', ' Galaxy', ' EcoSport',
    ' Mondeo', ' S-MAX', ' Tourneo Connect', ' Mustang',
    ' Puma', ' B-MAX', ' Streetka', ' Grand Tourneo Connect',
    ' Fusion', ' Ranger', ' Tourneo Custom', ' Transit Tourneo',
    ' Escort', 'Focus'
]

transmissions = ['Manual', 'Semi-Auto', 'Automatic']

fuel_types = ['Diesel', 'Petrol', 'Hybrid', 'Electric', 'Other']

# User inputs
car_model = st.selectbox("Car Model", car_models)

year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2026,
    value=2018,
    step=1
)

transmission = st.selectbox(
    "Transmission",
    transmissions
)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    value=30000,
    step=1000
)

fuel_type = st.selectbox(
    "Fuel Type",
    fuel_types
)

tax = st.number_input(
    "Tax",
    min_value=0.0,
    value=145.0
)

mpg = st.number_input(
    "MPG",
    min_value=0.0,
    value=50.0
)

engine_size = st.number_input(
    "Engine Size (Litres)",
    min_value=0.0,
    value=1.0,
    step=0.1
)

# Prediction
if st.button("Predict Price 🚀"):

    input_data = pd.DataFrame({
        'model': [car_model],
        'year': [year],
        'transmission': [transmission],
        'mileage': [mileage],
        'fuelType': [fuel_type],
        'tax': [tax],
        'mpg': [mpg],
        'engineSize': [engine_size]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Car Price: £{prediction[0]:,.2f}"
    )
    