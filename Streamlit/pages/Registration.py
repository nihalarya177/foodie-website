import streamlit as st
import pandas as pd
import numpy as np
from components import validate_username, user_controller

if 'selected_cuisines' not in st.session_state:
    st.session_state.selected_cuisines = None
if 'username' not in st.session_state:
    st.session_state.username = None
if 'submit' not in st.session_state:
    st.session_state.submit = None
if 'done' not in st.session_state:
    st.session_state.done = None
if 'cuisines' not in st.session_state:
    st.session_state.cuisines = None
if 'prices' not in st.session_state:
    st.session_state.prices = None

col1, col2, col3 = st.columns([2, 8, 2])

with col2:
    st.title("Welcome New User! :smile:")
       
    username_input = st.text_input("Enter a username")
    submitted = st.button("Submit")
    if submitted:
        if " " in username_input:
                st.warning("Username cannot contain spaces😱 Please enter a valid username😟")
        else:
            st.session_state.username = validate_username.validate_not_exists(st.session_state.user_data, username_input)
            if st.session_state.username is not None:
                st.session_state['username'] = username_input
                st.success(f"Username '{username_input}' created successfully! :white_check_mark:")
            else:
                st.warning(f"Sorry '{username_input}'  is already taken 😔")

            st.session_state['submit'] = submitted

    if st.session_state.username is not None:

        st.header("Select Your Cuisine Preferences: :pizza:")
        options = ['Italian', 'Chinese', 'Japanese', 'Indian']
        default_values = ['Italian', 'Indian']
        st.session_state.cuisines = st.multiselect("Select Your Favourite Cuisines! :heart_eyes_cat:", options, default=default_values)

        st.header("Select Your Prefered Price Range: :moneybag:")
        options = ['$$$', '$$', '$', '$-$$']
        default_values = ['$', '$$$']
        st.session_state.prices = st.multiselect("Select Your Favourite Cuisines! :heart_eyes_cat:", options, default=default_values)
        
        finished = st.button("Done")

        if finished:
            st.success(f"Thank You🙏 Set up Complete🥳 :white_check_mark:")
            st.session_state['done'] = finished
            st.session_state.user_dataframe = user_controller.add_new_user(st.session_state.username, st.session_state.cuisines, st.session_state.prices, st.session_state.credentials)
            st.session_state.user_data.append(st.session_state.username)
