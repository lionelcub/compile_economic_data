

import numpy as np
import pandas as pd

# For API request.
import requests
from time import time, sleep
from IPython.core.display import clear_output
from warnings import warn

# Personal modules. 
from configuration.config import url, params, sleep_time


# -------------------------------------------------------
# API Request. 
# -------------------------------------------------------

def collectFrom_multiAPI_endpoints(data_to_collect, dict_collected, dict_collected_keySet):
    for dataName, dict_data in data_to_collect.items():
        if dataName in dict_collected_keySet: 
            continue
        else:
            for key in dict_data.keys(): 
                params[key] = dict_data[key] 
            api_requests(url, params, dict_collected, dataName, sleep_time) 


def preprocess_dataAPI(df):
    df_copy = df.copy()
    
    # Convert date to datetime and set it as index. 
    df_copy['date'] = pd.to_datetime(df_copy['date'], yearfirst=True, infer_datetime_format=True)
    df_copy.set_index('date', inplace=True, drop=True)
    
    # Replace '.' with NaN. 
    df_copy['value'].replace('.', np.nan, inplace=True)
    df_copy['value'] = df_copy['value'].astype('float16')
    
    return df_copy


def api_requests(url, params, dict_df, dataName, sleep_time):
    '''
    Purpose: 
        Making API requests while taking the rate limit into account. 
    
    Input  :
        url        : Str. API endpoint.
        params     : Dict. Set of parameters for API endpoints. 
        dict_df    : Dict. To store the dataframes. 
        dataName   : Str. Name of the data. 
        sleep_time : Int. Pause duration. To avoid overloading the server. 

    Return :
        None.
    '''

    # Time the request to ensure it is staying within the rate limit.
    start = time() 
    
    response = requests.get(url, params=params)

    # Sleep for n seconds.
    sleep(sleep_time)
    elapsed_time = time() - start

    # Warn unsuccessful status code.
    if response.status_code != 200: 
        request_failed[dataName] = response.status_code
        warn(f'Request: {dataName}; Status code: {response.status_code}')

    # Append the items to the list if the request is successful.
    if response.status_code == 200:
        df = pd.DataFrame(response.json()['observations'])[['date','value']]

    # Print out the number of requests and time to monitor the progress.
    print(f"Request: {dataName}; Frequency: {elapsed_time}")
    clear_output(wait=True)
    
    # Preprocess the data and store the data into the dictionary. 
    try: dict_df[dataName] = preprocess_dataAPI(df)
    except: pass