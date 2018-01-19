import pandas as pd
import os
from IPython.display import display, HTML


def run():
    """ A function to run the script"""
    path = 'C:/Users/user/desktop/eng_dube/engineer_mdube/programming/datasets/2'
    filename = 'Customer Churn Model.txt'
    fullpath = os.path.join(path, filename)
    data_1 = pd.read_csv(fullpath)
    print("Data Frame 1:")
    display(data_1.head())
    display(data_1.columns.values)
    filename_2 = 'Physics_development_02Jan_to_28_Feb_2018.csv'
    path_2 = 'C:/Users/user/desktop/GDRIVETEMP/WIP/File sharing/'
    fullpath_2 = os.path.join(path_2, filename_2)
    data_2 = pd.read_csv(fullpath_2)
    print("Data Frame 2:")
    display(data_2)
    
run()