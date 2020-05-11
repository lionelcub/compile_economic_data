

import pickle

# Personal modules. 
from configuration.config import FRED_collection, FRED_data, request_failed
from autoprocess_FRED_API import api_request


# --------------------------------------------------------------
# Run.
# --------------------------------------------------------------

if __name__ == "__main__":
    commLine_input = input(
        '''
        Do you want to overwrite the entire FRED data you have? 
        Y:Yes   N:No   Q:Quit
        '''
    )

    if commLine_input == 'N':
        try: 
            with open('dataset/storage/FRED_data.pickle', 'rb') as in_file:
                FRED_data = pickle.load(in_file)
        except: print(
            """
            ERROR: 'dataset/storage/FRED_data.pickle' doesn't exist. 
            Will collect the entire FRED data. 
            """) 
        commLine_input = 'Run API'
    
    if commLine_input == 'Y' or  commLine_input == 'Run API': 
        # Run API requests. 
        api_request.collectFrom_multiAPI_endpoints(FRED_collection, FRED_data, set(FRED_data.keys()))
        
        print(f'Failed Request: {request_failed.keys()}\n')
        print(f'Compiled Data: {FRED_data.keys()}\n')

        # Save the dictionary containing all the dataframes in PICKLE format.  
        with open('dataset/storage/FRED_data.pickle', 'wb') as out_file: 
            pickle.dump(FRED_data, out_file) 