
import pandas as pd
from IPython.display import display, HTML
def run():
    data_1 = pd.read_csv(
        'C:/Users/user/desktop/ENG_DUBE/engineer_mdube/Programming/datasets/3/winequality-red.csv', sep=';'
        )
    print("Data Frame")    
    display(data_1.head())
    #print(HTML(data_1.to_html()))    
    
run()