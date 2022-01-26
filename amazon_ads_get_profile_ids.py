#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Jan 23 12:07:36 2022

@author: jonasschroeder
GitHub: https://github.com/JonasSchroeder
LinkedIn: https://www.linkedin.com/in/jonas-schröder-914a338a/

Please refer to the amazon ads api doc for further campaign report types

Note: You need to have registered as a developer to get your access token and refresh token.
Furthermore you need to know the profile id of the ads account you want the reports to download for.

Please read my blog post for further guidance:

This script (Jan 2022) expects v2 of the amazon ads api and might be outdated at the time of your use.

"""


import requests
import pandas as pd


REFRESH_TOKEN = "ADD_YOUR_REFRESH_TOKEN_HERE"
CLIENT_ID = "ADD_YOUR_CLIENT_ID_HERE"
CLIENT_SECRET = "ADD_YOUR_CLIENT_SECRET_HERE"

#----------------------------------------------------------------------------------------------------------------
# Step 1: Get a new access token
#----------------------------------------------------------------------------------------------------------------

def get_access_token(REFRESH_TOKEN):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }
    
    data = {
      'grant_type': 'refresh_token',
      'client_id': CLIENT_ID,
      'refresh_token': REFRESH_TOKEN,
      'client_secret': CLIENT_SECRET
    }
    
    response = requests.post('https://api.amazon.com/auth/o2/token', headers=headers, data=data)
    r_json = response.json()
    return r_json["access_token"]


#----------------------------------------------------------------------------------------------------------------
# Step 2: Get a list of profile ids associated with the developer account
#----------------------------------------------------------------------------------------------------------------

ACCESS_TOKEN = get_access_token(REFRESH_TOKEN)

headers = {
    'Amazon-Advertising-API-ClientId':CLIENT_ID,
    'Authorization': ACCESS_TOKEN
}


response = requests.get("https://advertising-api-eu.amazon.com/v2/profiles", headers=headers)

r_json = response.json()

# dataframe from json
profile_ids_df = pd.json_normalize(response.json())