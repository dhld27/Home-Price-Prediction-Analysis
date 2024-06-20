import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model
with open ('best_rf_model.pkl', 'rb') as model_file:
    modelRF = pickle.load(model_file)

def run():
    # Title
    st.title('House Pricing Prediction')

    st.write('Fill the form for your desired price of your house!')

    with st.form('House Price'):
        st.title('House')
        area = st.slider('Pick your area (square-feet)', min_value=1500, max_value=17000)
        bedrooms = st.slider('Choose the number of bedrooms', min_value=1, max_value=6)
        bathrooms = st.slider('Choose the number of bathrooms', min_value=1, max_value=4)
        stories = st.slider('Choose the stories of the house', min_value= 1, max_value=4)
        mainroad = st.radio('Connect to the mainroad?', ['yes', 'no'])
        guestroom = st.radio('Guestroom availability?', ['yes', 'no'])
        basement = st.radio('Basement availability?', ['yes', 'no'])
        hotWaterHeating = st.radio('Water Heater availability?', ['yes', 'no'])
        airCondition = st.radio('Air Conditioning availability?', ['yes', 'no'])
        parking = st.slider('Choose number of parking area', min_value=0, max_value=3)
        prefArea = st.radio('Preferred house area?', ['yes', 'no'])
        furnishingStatus = st.radio('Choose the furnishing status', ['furnished', 'semi-furnished', 'unfurnished'])
        st.markdown('====')
        submit = st.form_submit_button('Submit')
        # Create a new data

    dfInf = {
        'area': area,
        'bedrooms' : bedrooms,
        'bathrooms' : bathrooms,
        'stories' : stories,
        'mainroad' : mainroad,
        'guestroom': guestroom,
        'basement': basement,
        'hotwaterheating': hotWaterHeating,
        'airconditioning': airCondition,
        'parking': parking,
        'prefarea': prefArea,
        'furnishingstatus': furnishingStatus
    }

    dfInf = pd.DataFrame([dfInf])

    # Predict house's price

    predict = modelRF.predict(dfInf)

    if submit:
        st.write(f'House Price:{predict}')

if __name__ == '__main__':
    run()