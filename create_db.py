import pandas as pd



k=input("Please input a key: ") 
v=input("Plesse input a value: ") 


data = {'pi4': ['pi4','spare bedroom office desk'],'purple lamy':['purple lamy','spare bedroom office desk']}



df = pd.DataFrame.from_dict(data, orient="index", columns=['item','location'])

df.index.names = ['item']

df.columns = ['year','none']


df.columns()
df = df.reset_index()

data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}

df2 = pd.DataFrame.from_dict(data, orient='index',
                       columns=['A', 'B', 'C', 'D'])


