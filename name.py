import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import altair as alt

Stock_Market = {'Year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
                'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
                'EconomicGrowth_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
                'Unemployment_Rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
                'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]
}

#stock index price dependent on some favtors, dependent varoables, so on y-axis of graph or lhs of eqn

df = pd.DataFrame(Stock_Market,columns = ['Year','Month','EconomicGrowth_Rate','Unemployment_Rate','Stock_Index_Price'])
x = df[['EconomicGrowth_Rate','Unemployment_Rate']] #these are independent variables
y = df['Stock_Index_Price'] #these are dependent variables
lr = linear_model.LinearRegression() #library provides a linear_model library and Linearregression() a function
lr.fit(x,y) #fit to value x axis and y axis inside the model

st.title("Stock Index Prediction using Linear Regression")
st.text(" ")
st.text(" ")
st.text(" ")
st.image('stockindex.jpeg', width=700)
st.text(" ")
st.text(" ")
st.text(" ")

@st.cache_resource
def plot():
 st.subheader("Relationship between Stock Index Price and Economic Growth Rate")
st.text(" ")
st.text(" ")
st.text(" ")
plt.figure(figsize=(9,6))
plt.xlabel("Economic Growth Rate")
plt.ylabel("Stock Index Price")
plt.scatter(df['EconomicGrowth_Rate'],df['Stock_Index_Price'],color='g')
plt.tight_layout()
st.set_option('deprecation.showPyplotGlobalUse',False)
st.pyplot()
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")

st.subheader("Relationship between Stock Index Price and Unemployment Rate")
st.text(" ")
st.text(" ")
st.text(" ")
plt.figure(figsize=(9,6))
plt.xlabel("Unemployment Rate")
plt.ylabel("Stock Index Price")
plt.scatter(df['Unemployment_Rate'],df['Stock_Index_Price'],color='r')
plt.tight_layout()
st.set_option('deprecation.showPyplotGlobalUse',False)
st.pyplot()
st.text(" ")
st.text(" ")
st.text(" ")

plot()

e = st.number_input("Enter Economic Growth Rate")
st.text(" ")
u = st.number_input("Enter Unemployment Rate")
st.text(" ")

if st.button("Predict"):
 st.subheader("Predicted Value of Stock Index ")
st.text(lr.predict([[e,u]])[0])

#pip freeze > requirements.txt