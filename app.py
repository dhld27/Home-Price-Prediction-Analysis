import eda, predict
import streamlit as st

navigation = st.sidebar.selectbox('Navigation', ['EDA', 'House Pricing Prediction'])

st.sidebar.markdown('# About')
st.sidebar.write('''This application assists our clients in finding and purchasing a house in their desired area with additional rooms such as bedrooms and bathrooms, 
                    as well as stories and parking to fulfill their needs. It also helps them select the best location based on external factors such as 
                    the availability of guest rooms, proximity to main roads, water heating and air conditioning systems, and nearby amenities like schools, 
                    department stores, gyms, malls, airports, and public transportation (trains and buses). The app also takes into account whether the desired house 
                    is fully furnished, semi-furnished, or unfurnished to provide a comprehensive search result.''')

if navigation == 'EDA':
    eda.run()
else:
    predict.run()