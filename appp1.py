# Import the Libraries

import streamlit as st
#import pickle5 as pickle
import joblib
import numpy as np
import pandas as pd
from warnings import filterwarnings
filterwarnings('ignore')

# App Title

st.title('CONCRETE STRENGTH PREDICTION')


#[theme]
base="dark"
primaryColor="purple"

# Nice Concrete Photo

from PIL import Image
im = Image.open("concrete_static.jpg")
st.image(im, width = 400, caption = "concrete test")


#st.markdown(html_temp, unsafe_allow_html=True)

# Get the Input Values From Sidebar
st.sidebar.title('Please Enter the Following Parameters')

cement=st.sidebar.slider("Amount of Cement", 102, 540, step=5)
slag=st.sidebar.slider("Amount of Slag", 0,360, step=5)
flyash=st.sidebar.slider ("Amount of Flyash", 0,200, step=1)
water=st.sidebar.slider("Amount of Water", 120, 250, step=1)
superplasticizer=st.sidebar.slider ("Amount of Superplasticizer", 0, 32, step=1)
coarseaggregate=st.sidebar.slider ("Amount of Coarseaggregate", 800, 1145, step=1)
fineaggregate=st.sidebar.slider("Amount of Fineaggregate", 594, 993, step=1)
age=st.sidebar.slider("Age in Days", 1, 365, step=1)

# Prepare a Python Dictionary Using the Input Values and Convert to a DataFrame
st.markdown('ENTER THE QUANTITIES ADDED PER M3 TO GET THE APPROXIMATE STRENGTH OF CONCRETE ')
def csMPa():

    '''   my_dict = {"cement" :cement,
    "slag":slag,
    "flyash": flyash,
    "water": water ,
    "superplasticizer": superplasticizer,
    "coarseaggregate": coarseaggregate,
    "fineaggregate": fineaggregate,
    "age":age}'''

   
    test = np.array([[cement, slag, flyash, water, superplasticizer, coarseaggregate, fineaggregate,age]])


    #df_sample = pd.DataFrame.from_dict([test])
    # return df_sample
    #print(test)
    return test


dfc = csMPa()
#model = pickle.load(open("model.pkl", "rb"))
model = joblib.load('model.joblib') 
st.markdown('By-Rajesh Hugar')
st.markdown('Email_id-hugarrajesh@gmail.com')

if st.sidebar.button ("Submit"):


    result = (round(model.predict(dfc)[0],2))
    st.success(f"Compressive Strength Prediction of the Concrete is {result} MPa")
    
