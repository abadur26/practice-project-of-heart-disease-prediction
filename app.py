import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("Heart_Disease_Prediction.pkl","rb"))
scaler = pickle.load(open("Scaler.pkl", "rb"))

st.title("Heart Disease Prediction")
st.write("Fill the Following detils to predict if a persion have disease or not")
age = st.number_input("Age", 20,100)
sex = st.selectbox("Sex", [0,1], format_func=lambda x:"Female" if x ==0 else "Male")
cp = st.selectbox("Chest Pain Type(CP)", [0,1,2,3])
trestbps = st.number_input("Resting Blood Presser(trestbps)", 80,200)
chol = st.number_input("Cholesterol(chol)", 100,600)
fbs = st. selectbox("Fasting Blood Sugar>120 mg/dl(fbs)", [1,0])
restcg = st.selectbox("Resting ECG(restcg)",[0,1,2])
thalach = st.number_input("max Heart Rate Achived (thalach)", 60,250,150)
exang = st.selectbox("Exercise Include Angina (exange)",[0,1] )
oldpeak = st.number_input("St depression (oldpeak)", 0.0,6.0,1.0)
slope = st.selectbox("Slope of ST(slope)", [0,1,2])
ca = st.selectbox("Number of Major Vessels(ca)", [0,1,2,3,4])
thal = st.selectbox("Thalassemia (thal)", [0,1,2,3])
if st.button("Prediction"):
    input_data = np.array([[age,sex,cp,trestbps,chol,fbs, restcg,thalach, exang, oldpeak, slope, ca, thal]])
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)
    if prediction[0]==1:
        st.success("The Persion is likly to heart disease")
    else:
        st.success("The Persion is not likly to heart disease")