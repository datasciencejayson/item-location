import pandas as pd



k=input("Please input a key: ") 
v=input("Plesse input a value: ") 


data = {'pi4': 'spare bedroom office desk'}



df = pd.DataFrame.from_dict(data, orient="index", columns=['item','location'])

df
df.reset_index()

data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}

pd.DataFrame.from_dict(data, orient='index')