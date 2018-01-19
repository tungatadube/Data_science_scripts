import pandas as pd
import os
from IPython.display import display

def run():
    path = 'C:/Users/user/desktop/ENG_DUBE/engineer_mdube/programming/datasets/2'
    filename = 'titanic3.csv'
    fullpath = os.path.join(path, filename)
    data_1 = pd.read_csv(fullpath)
    display(data_1.head())
            
run()     
    
    