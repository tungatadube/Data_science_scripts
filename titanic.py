import pandas as pd
from IPython.display import display
def run():
    data = pd.read_csv(
    'C:/Users/user/Desktop/ENG_DUBE/engineer_mdube/Programming/datasets/2/titanic3.csv',
    )
    display(data.head())
    
run()

