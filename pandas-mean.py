import pandas as pd 

dataframe = pd.read_csv('data2.csv')
# mean() calculation
mean_of_data = dataframe["Calories"].mean()
print(mean_of_data) #304.68 replaced in callories empty cell 18th row

dataframe['Calories'].fillna(mean_of_data,inplace=True)
print(dataframe.to_string())