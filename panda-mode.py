import pandas as pd 

dataframe= pd.read_csv('data2.csv')

mode_of_dataframe = dataframe['Calories'].mode()[0]

print(mode_of_dataframe)

dataframe["Calories"].fillna(mode_of_dataframe,inplace=True)

print(dataframe)
