# Import the Libraries

import streamlit as st
import pickle
import pandas as pd
from warnings import filterwarnings
filterwarnings('ignore')


# Nice Concrete Photo

from PIL import Image
im = Image.open(r"https://github.com/rajeshXT/Concrete_strength.git")
st.image(im, width = 450, caption = "by Rajesh Hugar")

# App Title

html_temp = """
<div style="background-color:green;padding:1.5px">

<hi style="color: white;text-align:center;">Compresssive Strength Prediction </hl>
</div><br>"""

st.markdown (html_temp, unsafe_allow_html=True)

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

def csMPa():

    my_dict = {"cement" :cement,
    "slag":slag,
    "flyash": flyash,
    "water": water ,
    "superplasticizer": superplasticizer,
    "coarseaggregate": coarseaggregate,
    "fineaggregate": fineaggregate,
    "age":age}

    

    df_sample = pd.DataFrame.from_dict([my_dict])
    return df_sample


dfc = csMPa()
model = pickle.load(open("model.pkl", "rb"))


if st.sidebar.button ("Submit"):


    result = (model.predict (dfc))
    st.success(f"Compressive Strength Prediction of the Concrete is {result} MPa")
