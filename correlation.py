import pandas as pd 

data_set = pd.read_csv("data2.csv")


print(data_set.corr())