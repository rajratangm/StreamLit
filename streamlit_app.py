import streamlit as st
import pandas as pd 
st.title('🎈 Machine Learning App by Rajratan')
st.info('This is a practice app')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

st.write(df)
