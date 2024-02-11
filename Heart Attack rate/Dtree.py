import streamlit as st
import numpy as np
import pickle 

with open('./Dtree.pkl', 'rb') as file:
    model = pickle.load(file)
st.title('Heart Attack Prediction App for Decision Tree')
age = st.number_input('Enter the age', min_value=0)
sex = st.number_input('Enter The Gender: ', min_value=0, max_value=1, step=1)
cholestrol = st.number_input('Enter the cholestrol', min_value=0)
heartRate = st.number_input('Enter the HeartRate', min_value=0)
diabetes = st.number_input('Enter the diabetes', min_value=0)
familyHistory = st.number_input('Enter the FamilyHistory', min_value=0, max_value=1, step=1)
smoking = st.number_input('Enter the Smoking', min_value=0, max_value=1, step=1)
obasity = st.number_input('Enter the Obasity', min_value=0)
alcoholConsumption = st.number_input('Enter the alcohol Consumption', min_value=0)
exercisePerHour = st.number_input('Enter the exercise per hour', min_value=0)
diet = st.number_input('Enter the diet', min_value=0)
previousHeartProb = st.number_input('Enter the Previous Heart Problem', min_value=0)
medicationUse = st.number_input('Enter the Medication Use', min_value=0)
stressLevel = st.number_input('Enter the Stress Level', min_value=0)
sedentaryHoursPerDay = st.number_input('Enter the Sednetray Hours Per day', min_value=0)
BMI = st.number_input('Enter the BMI', min_value=0)
traglycerides = st.number_input('Enter the traglycerides', min_value=0)
physicalActivityDayPerWeek = st.number_input('Enter the Physical Activity Per week ', min_value=0)
sleepHours = st.number_input('Enter the Sleep Hours', min_value=0)
systolic = st.number_input('Enter the systolic', min_value=0)
diastolic = st.number_input('Enter the diastolys', min_value=0)
data = np.array([age, sex, cholestrol, heartRate, diabetes, familyHistory, smoking, obasity, alcoholConsumption, exercisePerHour
                 , diet, previousHeartProb, medicationUse, stressLevel, sedentaryHoursPerDay,  BMI, traglycerides, 
                 physicalActivityDayPerWeek, sleepHours, systolic, diastolic])
data = data.reshape(1,-1)
if st.button('Predict'):
    res = model.predict(data)

    if res == 0:
        st.write('Congratulation. You are healthy')
    else:
        st.write("sorry!, You have heart attack risk.")

