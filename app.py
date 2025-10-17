# -*- coding: utf-8 -*-


import numpy as np
import streamlit as st
import pickle

with open(r"cancer_patient_prediction_data.sav", 'rb') as file:
    model = pickle.load(file)
    
# Load the trained model
##with open('cancer_patient_prediction_data.sav', 'rb') as file:
   ## model = pickle.load(file)

# Streamlit UI
st.title("cancer_patient_prediction_data")
st.write("Fill the following information to get a prediction:")

# User Inputs
index = st.number_input("index", value=0.0)
Patient_Id = st.number_input("Patient Id", value=0.0)
Age = st.number_input("Age", value=0.0)
Gender = st.number_input("Gender", value=0.0)
Air_Pollution = st.number_input("Air Pollution", value=0.0)
Alcohol_use = st.number_input("Alcohol use", value=0.0)
Dust_Allergy = st.number_input("Dust Allergy", value=0.0)
OccuPational_Hazards = st.number_input("OccuPational Hazards", value=0.0)
Genetic_Risk = st.number_input("Genetic_Risk", value=0.0)
chronic_Lung_Disease = st.number_input("chronic_Lung_Disease", value=0.0)
Fatigue = st.number_input("Fatigue", value=0.0)
Weight_Loss = st.number_input("Weight Loss", value=0.0)
Shortness_of_Breath = st.number_input("Shortness of Breath", value=0.0)
Wheezing = st.number_input("Wheezing", value=0.0)
Swallowing_Difficulty = st.number_input("Swallowing_Difficulty", value=0.0)
Clubbing_of_Finger_Nails = st.number_input("Clubbing_of_Finger Nails", value=0.0)
Frequent_Cold = st.number_input("Frequent_Cold", value=0.0)
Dry_Cough = st.number_input("Dry_Cough", value=0.0)
Snoring = st.number_input("Snoring", value=0.0)


# Prediction on button click
if st.button("Predict"):
    # Create input in correct order and shape
    Input = np.array([[index, Patient_Id, Age, Gender, Air_Pollution, Alcohol_use , Dust_Allergy, OccuPational_Hazards, Genetic_Risk, chronic_Lung_Disease,
                       Fatigue, Weight_Loss, Shortness_of_Breath, Wheezing, Swallowing_Difficulty,Clubbing_of_Finger_Nails, Frequent_Cold, Dry_Cough, Snoring]])
    
    # Predict
    prediction = model.predict(Input)
    
    # Show result
    st.success(f"cancer patient Predicted data is : {prediction[0]:.2f}")

