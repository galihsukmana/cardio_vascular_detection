import streamlit as st
import pandas as pd
import pickle
import joblib

st.title("Cardio Vascular Disease Detection")
st.write("""
Created by Galih S
""")

# import model
model = pickle.load(open("full_pipe.pkl", "rb"))



st.write('Insert feature below to predict')

# user input
age = st.number_input(label='Age', min_value=30, max_value=65, value=30, step=1)
gender = st.selectbox(label='Gender', options=['male','female'])
height = st.number_input(label='Height', min_value=55, max_value=207, value=55, step=1)
weight = st.number_input(label='Weight', min_value=10, max_value=200, value=10, step=1)
ap_hi = st.number_input(label='Systolic blood pressure', min_value=-150, max_value=16020, value=120, step=1)
ap_lo = st.number_input(label='Diastolic blood pressure', min_value=-70, max_value=11000, value=80, step=1)
cholesterol	= st.selectbox(label='Cholesterol (1: normal, 2: high, 3: very high )', options=[1,2,3])
gluc = st.selectbox(label='Glucose (1: normal, 2: high, 3: very high )', options=[1,2,3])
smoke	= st.selectbox(label='Smoking (0 : passive & 1 : active)', options=[0,1])
alco	= st.selectbox(label='Alcohol Intake (0 : none & 1 : active)', options=[0,1])
active = st.selectbox(label='Physical Activity (0 : innactive & 1 : active)', options=[0,1])

# convert into dataframe
data = pd.DataFrame({'age': [age],
                'gender': [gender],
                'height': [height],
                'weight':[weight],
                'ap_hi': [ap_hi],
                'ap_lo': [ap_lo],
                'cholesterol': [cholesterol],
                'gluc': [gluc],
                'smoke': [smoke],
                'alco': [alco],
                'active':[active]})

# model predict
if st.button('Predict'):
    pred = model.predict(data).tolist()[0]

    if pred == 1:
        pred = 'Detected'
    else:
        pred = 'None'

    st.write('Based on your condition, the result is: ')
    st.write(pred)
