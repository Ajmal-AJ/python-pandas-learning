import pandas as pd 

dataframe =pd.read_csv('data2.csv')
print(dataframe)

for x in dataframe.index:
    if dataframe.loc[x,"Duration"] >120:
        dataframe.drop(x, inplace=True)
print(dataframe)