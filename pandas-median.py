import pandas as pd 

dataframe = pd.read_csv('data2.csv')

median_of_data = dataframe["Calories"].median()
dataframe['Calories'].fillna(median_of_data,inplace=True)

print(median_of_data)
print(dataframe)
