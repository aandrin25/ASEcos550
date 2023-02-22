###########################
# Import Libraries
###########################

import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import os
import base64
import pickle

##################################################################################################################################

## Molecular descriptor calculator
#def desc_calc():
##    # Performs the descriptor calculation
#    bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
#    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#    output, error = process.communicate()
#    os.remove('molecule.smi')

##################################################################################################################################

# File download
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href

##################################################################################################################################

###########################
## Model building
###########################

@st.cache_data
def build_model(input_data):
    # Reads in saved regression model
    load_model = pickle.load(open('model.pkl', 'rb'))
    # Apply model to make predictions
    prediction = load_model.predict(input_data)
    st.header('**Prediction output**')
    prediction_output = pd.Series(prediction, name='Suicide attempt')
    molecule_name = pd.Series(load_data[1], name='molecule_name')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)

##################################################################################################################################



##################################################################################################################################


# Logo image
image = Image.open('Aesthetic Twitter Header.png')

st.image(image, use_column_width=True)

# Page title
st.markdown("""
# But Will It Kill Me App
This app allows you to predict the liklihood of suciidal ideations postnatal.Are you a new mom struggling with postpartum depression and worried about your risk of suicide? This web application uses data from a “medical hospital's questionnaire, administered through a Google form”, to provide you with an estimate of your likelihood of suicide based on your answers to a series of questions. With a dataset of 1503 records, the algorithm can analyze your responses and generate a personalized report on your risk of suicide. Our easy-to-use and confidential platform provides you with valuable insights and guidance to help you act and get the support you need to manage your mental health. 


**Credits**
- App built in `Python` + `Streamlit` by Averya Andrin (https://nadrinetwork.com) 


---
""")

##################################################################################################################################

###########################
## Question Selection
###########################

st.subheader('Start by Answering the Questions Below')

with st.form("my_form"):
   st.write("With which age group do you most identify?")
   st.selectbox('Select One', ['25 to 30', '30 to 35', '35 to 40', '40 to 45', '45 to 50'])
   st.write("Have you felt sad since having your baby?")
   st.selectbox('Select One', ['Yes', 'No'])
   st.write("Have you been irritable towards your baby or partner?")
   st.selectbox('Select One', ['Yes', 'No'])
   st.write("Have you had trouble sleeping at night?")
   st.selectbox('Select One', ['Yes', 'No'])
    
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   


st.text('Outside the Form')


##################################################################################################################################


st.write("Resources")
