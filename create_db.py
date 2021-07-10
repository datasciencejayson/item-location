import pandas as pd



k=input("Please input a key: ") 
v=input("Plesse input a value: ") 


item_dict = {'pi4': ['pi4','spare bedroom office desk'],'purple lamy':['purple lamy','spare bedroom office desk']}


def make_df():
    temp_df = pd.DataFrame.from_dict(item_dict, orient="index", columns=['item','location'])
    return temp_df

def dict_entry():
    k=input("Please input a key: ") 
    v=input("Plesse input a value: ") 
    item_dict[k] = [k,v]


def enter_new_item():
    dict_entry()
    make_df()
    return make_df()

df.to_excel('C:/Users/jbackes/Documents/personal/item-location/item_location.xlsx')
del item_dict['new']

df = enter_new_item()


df = make_df()

df.index.names = ['item']

df.columns = ['year','none']


df.columns()
df = df.reset_index()

data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}

df2 = pd.DataFrame.from_dict(data, orient='index',
                       columns=['A', 'B', 'C', 'D'])


