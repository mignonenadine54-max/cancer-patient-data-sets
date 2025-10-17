


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
Age = st.number_input("Age", value=33)
Gender = st.number_input("Gender", value=1)
Air_Pollution = st.number_input("Air Pollution", value=2)
Alcohol_use = st.number_input("Alcohol use", value=4)
Dust_Allergy = st.number_input("Dust Allergy", value=5)
OccuPational_Hazards = st.number_input("OccuPational Hazards", value=4)
Genetic_Risk = st.number_input("Genetic_Risk", value=3)
chronic_Lung_Disease = st.number_input("chronic_Lung_Disease", value=2)

Balanced_Diet = st.number_input("Balanced_Diet'", value=2)
Obesity = st.number_input("Obesity", value=4)
Smoking = st.number_input("Smoking", value=3)
Passive_Smoker= st.number_input("Passive Smoker", value=2)
Chest_Pain = st.number_input("Chest Pain", value=2)
Coughing_of_Blood = st.number_input("Coughing_of_Blood ", value=4)

Fatigue = st.number_input("Fatigue", value=3)
Weight_Loss = st.number_input("Weight Loss", value=4)
Shortness_of_Breath = st.number_input("Shortness of Breath", value=2)
Wheezing = st.number_input("Wheezing", value=2)
Swallowing_Difficulty = st.number_input("Swallowing_Difficulty", value=3)
Clubbing_of_Finger_Nails = st.number_input("Clubbing_of_Finger Nails", value=4)
Frequent_Cold = st.number_input("Frequent_Cold", value=1)
Dry_Cough = st.number_input("Dry_Cough", value=3)
Snoring = st.number_input("Snoring", value=4)


# Prediction on button click
if st.button("Predict"):
    # Create input in correct order and shape
    Input = np.array([[index, Patient_Id, Age, Gender, Air_Pollution, Alcohol_use , Dust_Allergy, OccuPational_Hazards, Genetic_Risk, chronic_Lung_Disease,
                       Balanced_Diet,Obesity,Smoking,Passive_Smoker,Chest_Pain,Coughing_of_Blood,Fatigue, Weight_Loss, Shortness_of_Breath, Wheezing, Swallowing_Difficulty,Clubbing_of_Finger_Nails, Frequent_Cold, Dry_Cough, Snoring]])
    
    # Predict
    prediction = model.predict(Input)
    
    # Show result
    st.success(f"cancer patient Predicted data is : {prediction[0]:.2f}")
