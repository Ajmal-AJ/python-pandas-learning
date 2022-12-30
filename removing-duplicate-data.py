import pandas as pd 

dataframe =pd.read_csv('data2.csv')
'''check duplicate data occure  use duplicated() method'''
print(dataframe.duplicated())

''' now remove duplicate data  use drop_duplicates() method. '''
dataframe.drop_duplicates(inplace=True)
print(dataframe)
