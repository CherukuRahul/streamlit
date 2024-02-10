import streamlit as st
import pandas as pd
import numpy as np

st.title("Day-5")

st.text("We are going to learn about the area_chart function in the st")
code = '''
st.area_chart(
    data=None,
    *,
    x=None, 
    y=None, 
    color=None, 
    width=0, 
    height=0, 
    use_container_width=True )
'''
st.code(code, language = 'python', line_numbers = True)
st.text("This the sample dataset just taken for better understanding")
st.divider()
file_path = r"C:\Users\C ARAVIND\Downloads\India_Updated Literacy 2021.csv"
data = pd.read_csv(file_path)
st.dataframe(data)
st.divider()
st.scatter_chart(data, x = "States/UTs", y = "Children age 5 years who attended pre-primary school ", color = "Area")