import pandas as pd 

dataframe =pd.read_csv('data2.csv')
dataframe['Date'] = pd.to_datetime(dataframe['Date'])
print(dataframe.to_string())

print("\nNaT value remove use row remove\n")

dataframe.dropna(subset=["Date"],inplace=True)
print(dataframe)