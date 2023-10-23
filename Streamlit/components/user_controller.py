import pandas as pd
import pandas_gbq

def get_users(credentials):
    df = pandas_gbq.read_gbq(
        "SELECT user_name, cuisine_preference, price_preference FROM `foodie.Users`",
        project_id='black-machine-400914',
        credentials=credentials,
    )
    return df['user_name'].tolist()

def get_current_user(username, credentials):
    df = pandas_gbq.read_gbq(
        "SELECT user_name, cuisine_preference, price_preference FROM `foodie.Users`",
        project_id='black-machine-400914',
        credentials=credentials,
    )
    return df[df['user_name']==username]

def add_new_user(username, cuisines, prices, credentials):
    cuisine_pref = ''
    for cuisine in cuisines:
        cuisine_pref = cuisine_pref+cuisine+','
    cuisine_pref = cuisine_pref[:-1]
    price_pref = ''
    for price in prices:
        price_pref = price_pref+price+','
    price_pref = price_pref[:-1]
    df = pd.DataFrame({'user_name':username, 'cuisine_preference':cuisine_pref, 'price_preference':price_pref}, index=[0])
    pandas_gbq.to_gbq(
        df, 'foodie.Users', project_id='black-machine-400914', if_exists='append',credentials=credentials
    )
    return df
    
