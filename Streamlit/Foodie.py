import streamlit as st
import pandas as pd
from components import validate_username, google_connector, user_controller

if "credentials" not in st.session_state:
    st.session_state.credentials = google_connector.authenticate_google()
if "user_dataframe" not in st.session_state:
    st.session_state.user_dataframe = None
if "user_data" not in st.session_state:
    st.session_state.user_data = user_controller.get_users(st.session_state.credentials)
if "username" not in st.session_state:
    st.session_state.username = None
if 'login_button' not in st.session_state:
    st.session_state.login_button = None

st.set_page_config(
    page_title="Foodie",
    page_icon="🍔🍜🍩",
    layout="wide"
)

st.title("Welcome to Foodie!🍔🍜🍩")

col1, col2, col3 = st.columns([8, 2, 1])

with col1:
    st.write("Your very own personalised restaurant recommendation Engine")
    if st.session_state['username'] is None:
        st.write("To start off, please log in so we can get your past recommendations before we start")
    else:
        st.write(f"Welcome to Foodie {st.session_state.username}! :smile:")

with col2:
    text_input = st.text_input("Please enter Username👇", placeholder="Username")
    if st.button("Submit"):
        st.session_state.login_button = 'login attempted'
        st.experimental_rerun()
       
    if text_input:
        if st.session_state.login_button is not None and st.session_state.username is None:
            st.write('sorry we did not find that username, please register on our register page')
        st.session_state.username = validate_username.validate_exists(st.session_state.user_data, text_input)
        if st.session_state.username is not None:
            st.session_state.user_dataframe = user_controller.get_current_user(st.session_state.username, st.session_state.credentials)
            start_time, end_time = st.select_slider(
                'Select a range of time 🕒',
                options=['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30', '00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30'],
                value=('9:30', '17:30'))
            st.write('You selected **', start_time, '** and **', end_time, '**')

    if st.session_state.username is not None:
            st.session_state.user_dataframe = user_controller.get_current_user(st.session_state.username, st.session_state.credentials)
            start_time, end_time = st.select_slider(
                'Select a range of time 🕒',
                options=['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30', '00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30'],
                value=('9:30', '17:30'))
            st.write('You selected **', start_time, '** and **', end_time, '**')

            
        
        

