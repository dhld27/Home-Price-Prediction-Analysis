# streamlit
import streamlit as st
# pandas
import pandas as pd
# Visualisation
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
# Image
from PIL import Image

def run():
    # Create Title
    st.title('California House Price Prediction')
    # Create Introduction
    st.subheader('Introduction')
    # Create Preliminary 
    st.write("House in California.")
    # Add an image from URL
    st.image('https://www.ppic.org/wp-content/uploads/suburban-homes-768x512.jpg')
    # Create caption
    st.caption("source: PPIC (Public Policy Institute of California)")

    # Description
    st.write('## Objective')
    st.write('''
        The dataset seems decent to use a model of regression. 
        Therefore, this task tended to predict the price of a desire house to a client 
        with various additional facility such as 
        area (square feet), bedrooms, bathrooms, guest room, stories, parking, water heater, air conditioning, furnishing status, 
        and location such as main road connection, and preferred area that matched with the client's budget.
    ''')
    st.write('## Problem Statement')
    st.write('''
        Based on the written objective, the task tended to pick the best among five
        models between K-Neighbors Regressor, SVR, Decision Tree Regressor, 
        Random Forest Regressor, and Gradient Boost to predict the price for a house that 
        matches to a client based on their desire, budget, and so on.  
    ''')

    st.divider()
    # Display the DataFrame
    st.write('## Data')
    df = pd.read_csv('Housing.csv')
    st.dataframe(df)
    st.write('Dataset Description')
    '''
        The dataset obtained from Kaggle for improving the
        Machine Learning knowledge's improvement
    '''

    st.divider()

    # Visualisation
    st.write('## Exploratory Data Analysis')
    # Display the plots

    # Scatterplot
    st.write('### Furnishing Status of House Scatterplot')
    fig = plt.figure(figsize=(10, 6))
    sns.scatterplot(x="area", y="price", hue='furnishingstatus', data=df, palette='colorblind')
    plt.xlabel("Area")
    plt.ylabel("Price")
    plt.title("Area vs. Price")
    st.pyplot(fig)

    # Barplot
    st.write('### Average Price of House by Bedrooms & Furnishing Status')
    fig1 = plt.figure(figsize=(10, 6))
    sns.barplot(x="bedrooms", y="price", hue="furnishingstatus", data=df)
    plt.xlabel("Bedrooms")
    plt.ylabel("Average Price")
    plt.title("Average Price of House by Bedrooms and Furnishing Status")
    st.pyplot(fig1)

    # 2nd Barplot
    st.write('Average House Price by Bathrooms & Furnishing Status')
    fig2 = plt.figure(figsize=(10, 6))
    sns.barplot(x="bathrooms", y="price", hue="furnishingstatus", data=df)
    plt.xlabel("Bathrooms")
    plt.ylabel("Average Price")
    plt.title("Average House Price by Bathrooms and Furnishing Status")
    st.pyplot(fig2)

    # 3rd Barplot
    st.write('### Average Price by Guest Room & Furnishing Status')
    fig3 = plt.figure(figsize=(10, 6))
    sns.barplot(x="guestroom", y="price", hue="furnishingstatus", data=df)
    plt.xlabel("Guest Room")
    plt.ylabel("Average Price")
    plt.title("Average Price by Guest Room and Furnishing Status")
    st.pyplot(fig3)

    # 4th Barplot
    st.write('### Average Price of Houe by Stories & Furnishing Status')
    fig4 = plt.figure(figsize=(10, 6))
    sns.barplot(x="stories", y="price", hue="furnishingstatus", data=df)
    plt.xlabel("Stories")
    plt.ylabel("Average Price")
    plt.title("Average Price of House by Stories and Furnishing Status")
    st.pyplot(fig4)

    # 5th Barplot
    st.write('### Average Price of House by Main Road & Furnishing Status')
    fig5 = plt.figure(figsize=(10, 6))
    sns.barplot(x="mainroad", y="price", hue="furnishingstatus", data=df)
    plt.xlabel("Main Road")
    plt.ylabel("Average Price")
    plt.title("Average Price of house by Main Road and Furnishing Status")
    st.pyplot(fig5)

    # 6th Barplot
    st.write('### Average Prie of House by Air Conditioning & Furnishing Status')
    fig6 = plt.figure(figsize=(10,6))
    sns.barplot(x="airconditioning", y="price", hue="furnishingstatus", data=df)
    plt.xlabel("Air Conditioning")
    plt.ylabel("Average Price")
    plt.title("Average Price of house by Air Conditioning and Furnishing Status")
    st.pyplot(fig6)

    # 7th Barplot
    st.write('### Count of Houses based on Furnishing Status')
    fig7 = plt.figure(figsize=(8, 6))
    sns.countplot(x="furnishingstatus", data=df)
    plt.xlabel("Furnishing Status")
    plt.ylabel("Count")
    plt.title("Count of Houses Furnishing Status")
    st.pyplot(fig7)

if __name__ == '__main__':
    run()
