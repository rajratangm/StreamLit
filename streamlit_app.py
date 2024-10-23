import streamlit as st
import pandas as pd

# # Function to display the Home page content
# def home_page():
#     st.title('🎈 Machine Learning App by Rajratan')
#     st.info('This is a practice app')
    
#     with st.expander('Data'):
#         st.write('**Raw Data**')
#         df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
#         st.write(df)

#         st.write('**X**')
#         X = df.drop('species', axis=1)
#         st.write(X)

#         st.write('**y**')
#         y_raw = df.species
#         st.write(y_raw)

#     with st.expander('Data visualization'):
#         st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

#     # Sidebar inputs for the machine learning model
#     with st.sidebar:
#         st.header('Input Features')
#         island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
#         bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
#         bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
#         flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
#         body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
#         gender = st.selectbox('Gender', ('male', 'female'))

#         data = {
#             'island': island,
#             'bill_length_mm': bill_length_mm,
#             'bill_depth_mm': bill_depth_mm,
#             'flipper_length_mm': flipper_length_mm,
#             'body_mass_g': body_mass_g,
#             'sex': gender
#         }

#         input_df = pd.DataFrame(data, index=[0])
#         input_penguins = pd.concat([input_df, X], axis=0)

#     # Encoding the categorical columns
#     encode = ['island', 'gender']
#     df_penguins = pd.get_dummies(input_penguins, prefix=encode)

#     # Target mapper for species
#     target_mapper = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
#     def target_encoder(val):
#         return target_mapper[val]

#     y = y_raw.apply(target_encoder)

#     with st.expander('Input features'):
#         st.write('**Input data**')
#         st.write(input_df)
#         st.write('**Combined Penguin Data**')
#         st.write(input_penguins)
#         st.write('Encoded input Penguins')

# # Function to display the New Page content
# def new_page():
#     with st.sidebar:
#         st.checkbox('Show inputs only')
#         st.selectbox('select a job', ['job1', 'job2','job3'])
#         st.selectbox('select scenarios', ['scenario1','scenario2','scenario3'])
#         st.checkbox('compare two jobs')
#         st.checkbox('select all areas')
#         st.multiselect('select areas',['Tko','tmo','kto'])
                 
#     st.title('Welcome to the New Page!')
#     st.write('This is another page. You can put any content here.')
#     st.write('Go back to the **Home** page using the sidebar buttons.')
# def new_page1():
#     st.title('Welcome to the New Page1!')
#     st.write('This is another page1111. You can put any content here.')
#     st.write('Go back to the **Home** page using the sidebar buttons.')
    

# # Sidebar navigation buttons
# with st.sidebar:
#     st.header('Navigation')
#     if st.button('Home'):
#         st.session_state.page = 'Home'
#     if st.button('New Page'):
#         st.session_state.page = 'New Page'
#     if st.button('New1'):
#         st.session_state.page='new1'

# # Set default page if session state does not exist
# if 'page' not in st.session_state:
#     st.session_state.page = 'Home'

# # Render the page content based on which button is clicked
# if st.session_state.page == 'Home':
#     home_page()
# elif st.session_state.page == 'New Page':
#     new_page()
# elif st.session_state.page=='new1':
#     new_page1()

import streamlit as st

# Define the tooltip text
tooltip_text = "Click this button to perform an action."

# Display button with a tooltip
if st.button('Hover me!'):
    st.success('Button clicked!')

# Display the tooltip information using markdown
st.markdown(
    f"""
    <style>
    .tooltip {{
        position: relative;
        display: inline-block;
        cursor: pointer;
    }}
    .tooltip .tooltiptext {{
        visibility: hidden;
        width: 120px;
        background-color: black;
        color: #fff;
        text-align: center;
        border-radius: 5px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        bottom: 125%; /* Position above the button */
        left: 50%;
        margin-left: -60px;
        opacity: 0;
        transition: opacity 0.3s;
    }}
    .tooltip:hover .tooltiptext {{
        visibility: visible;
        opacity: 1;
    }}
    </style>
    <div class="tooltip">
        Hover me!
        <span class="tooltiptext">{tooltip_text}</span>
    </div>
    """,
    unsafe_allow_html=True
)




