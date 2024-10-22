import streamlit as st
import pandas as pd 
st.title('🎈 Machine Learning App by Rajratan')
st.info('This is a practice app')
with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  
  X = df.drop('species', axis=1)
  X 
  st.write('**y**')
  y_raw = df.species
  y_raw

with st.expander('Data visualization'):
  st.scatter_chart(data=df,x='bill_length_mm', y= 'body_mass_g', color= 'species')

# Data Preprations

with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('male', 'female'))
  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X], axis=0)
# Encoding x
encode = ['island', 'gender']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)
# prepare y 
target_mapper = {'Adelie': 0,
                 'Chinstrap': 1,
                 'Gentoo': 2}
def target_encoder(val):
  return target_mapper[val]
y = y_raw.apply(target_encoder)
y
  
with st.expander('Input features'):
  st.write('**Input data**')
  input_df
  st.write('**Combined Penguin Data**')
  input_penguins
  st.write('Encoded input Penguins')


