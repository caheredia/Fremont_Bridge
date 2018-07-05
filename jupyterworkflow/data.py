from urllib.request import urlretrieve
import os
import pandas as pd 

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename= 'Fremont.csv', url=FREMONT_URL, force_download = 
False):
    '''Download and cache the Fremont data

    Parameters
    ----------
    filename : string (optional)
    	location to save the data 
    url : string (optional) 
    	web location of the data
    force_download : bool (optional)
    	if TRUE, then force data download

    Returns
    -------
    data : pandas.DataFrame
    	The Fremont Bridge data
    '''
    if not os.path.exists(filename) or force_download:
        urlretrieve(URL, 'Fremont.csv')
    data = pd.read_csv('Fremont.csv', index_col='Date')
    data.columns = ['East', 'West']
    data['Total'] = data['East'] + data['West']
    try: 
        data.index = pd.to_datetime(data.index, format = '%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)
    return data
