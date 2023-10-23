import pandas as pd
import streamlit as st

def validate_exists(user_list, username):
    if username in user_list:
        return username
    else:
        return None
    
def validate_not_exists(user_list, username):
    if username in user_list:
        return None
    else:
        return username