import streamlit as st
import pickle
import numpy as np

# Load the scaler and model
scaler = pickle.load(open("Models/Diabetes_Standard_Scaler.pkl", "rb"))
model = pickle.load(open("Models/Diabetes_Prediction_model.pkl", "rb"))

# App Title
st.title("Diabetes Prediction App")

# Sidebar for user input
st.sidebar.header("Input Parameters")
def user_input_features():
    Pregancies = st.sidebar.number_input("Pregnancies", min_value=0, max_value=20, value=0)
    Glucose = st.sidebar.number_input("Glucose", min_value=0, max_value=200, value=120)
    BloodPressure = st.sidebar.number_input("Blood Pressure", min_value=0, max_value=200, value=80)
    SkinThickness = st.sidebar.number_input("Skin Thickness", min_value=0, max_value=99, value=20)
    Insulin = st.sidebar.number_input("Insulin", min_value=0, max_value=900, value=30)
    BMI = st.sidebar.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0, format="%.1f")
    DiabetesPedigreeFunction = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=10.0, value=0.5, format="%.2f")
    Age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=30)
    
    data = {
        "Pregancies": Pregancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }
    features = np.array([[Pregancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    return data, features

# Get user input
input_data, input_features = user_input_features()

# Display user input
st.write("## Input Parameters")
st.write(input_data)

# Prediction
if st.button("Predict"):
    scaled_data = scaler.transform(input_features)
    prediction = model.predict(scaled_data)
    
    result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"
    st.write(f"## Prediction: {result}")
