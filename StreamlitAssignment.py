import streamlit as st
import pandas as pd 
from models.dummies import *
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pickle
import logging 
import numpy as np
import warnings 
warnings.filterwarnings("ignore")

models_path= "models/"
data_path="data/"
model_name= "linear_regression_model_2.h5"

model_file=open(models_path+model_name, 'rb');

model = pickle.load(model_file)


st.title("Calculating Insurance Charges")

st.header("Enter the values:")

## Continous data number input
age=st.number_input('Enter the age: ',value=0)
children_number=st.number_input('Enter children number: ',value=0)
bmi = st.number_input("Enter the body mass index: ",value=20.0)
st.write("BMI is calaculated by dividing mass in kilograms by height in meters squared")

## Categorical data select boxes 
gender_selected=st.selectbox('Gender? ',['male','female']) 
gender=gender_dummies[gender_selected]

smoker_selected=st.selectbox('smoker? ',['yes','no']) 
smoker=smoker_dummies[smoker_selected]

region_selected=st.selectbox('Region? ',['southeast','southwest','northeast','northwest'])
region=region_dummies[region_selected]


data=[age,children_number,bmi,gender,smoker]
data=data+region

#st.write(data)



try:
    result=model.predict(np.array([data]))
    st.header("Expected Charges: ")
    st.write(result)
except Exception as e:
    st.write("Something occurs when showing results")
    logging.error("Exception occurs",exc_info=True)
   

