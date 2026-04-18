import streamlit as st
import pandas as pd
import joblib

st.title("Breast Cancer Detection System")          
st.header("Enter Patient information") 
features = joblib.load('/model/features.pkl')
scalar = joblib.load('/model/scaler.pkl')
model = joblib.load('/model/breast_cancer_model.pkl')
user_input = {}
for i in features:
    user_input[i] = st.number_input(i,value=0.0)

button = st.button('Predict')
if button == True:
    df = pd.DataFrame([user_input])
    scaled_df = scalar.transform(df)
    pred = model.predict(scaled_df)
    if pred[0] == 0:
        st.success(" Benign — No Cancer Detected")
    elif pred[0] == 1:
        st.error(" Malignant — Cancer Detected. Please consult a doctor immediately.")

st.caption("Built by Saim | SVC Model | Acc: 96%") 
