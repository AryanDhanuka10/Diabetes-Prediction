# Diabetes Prediction App

![Diabetes Prediction](https://imgs.search.brave.com/6sAswEgHcrcMLnHmTMfzfweG5QgDm28525gfAk_SyEc/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTEy/OTQxMzEyNi9waG90/by9kaWFiZXRlcy1k/b2luZy1ibG9vZC1n/bHVjb3NlLW1lYXN1/cmVtZW50LmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz1yQURU/NHpkQjJXT3drdFlL/X3d5R1pLZFp5aVNN/YTRjdmVZTFhTZXJy/VTlZPQ)

## Overview
The **Diabetes Prediction App** is a machine learning-powered web application designed to predict whether a person is diabetic or not based on various health metrics. Built using Python, Streamlit, and scikit-learn, the app allows users to input health parameters or load models to get instant predictions.

🌐 **Deployed App:** [Diabetes Prediction App](https://diabetes-prediction-aryan-dhanuka.streamlit.app/)

---

## Features
- **User-Friendly Input**: Easily input health metrics like glucose levels, BMI, and age.
- **Real-Time Prediction**: Get instant predictions of "Diabetic" or "Non-Diabetic."
- **Interactive UI**: Responsive and intuitive interface built with Streamlit.
- **Scalable Model**: Uses machine learning models to ensure accurate predictions.

---

## Input Parameters
The app accepts the following inputs:
- **Pregnancies**: Number of times the patient has been pregnant.
- **Glucose**: Plasma glucose concentration.
- **Blood Pressure**: Diastolic blood pressure (mm Hg).
- **Skin Thickness**: Triceps skin fold thickness (mm).
- **Insulin**: 2-Hour serum insulin (mu U/ml).
- **BMI**: Body mass index (weight in kg/height in m²).
- **Diabetes Pedigree Function**: Diabetes pedigree function (genetic risk score).
- **Age**: Age of the patient.

---

## How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AryanDhanuka10/Diabetes-Prediction
   cd Diabetes-Prediction
   ```

2. **Install Dependencies**
   Ensure you have Python 3.7+ installed. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**
   ```bash
   streamlit run application.py
   ```

4. Open the app in your browser at `http://localhost:8501`.

---

## Built With
- **Python**: Core programming language.
- **Streamlit**: For building interactive web apps.
- **scikit-learn**: For machine learning model development.
- **Pandas & NumPy**: Data processing libraries.

---

## Future Improvements
- Add advanced visualizations for predictions.
- Include options for loading user datasets.
- Support additional disease predictions.

---

## Contributing
Contributions are welcome! Please open an issue or create a pull request for suggestions and improvements.
