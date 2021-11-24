import pandas as pd

def get_data(fp):
    '''
    Retrieve data from filepath and loads it 
    into a pandas dataframe.
    '''  
    
    data = pd.read_csv(fp)
    
    return data
