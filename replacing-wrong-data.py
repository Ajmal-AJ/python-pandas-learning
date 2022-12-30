import pandas as pd 
 
dataset = pd.read_csv("data2.csv")
print("\n =======================wrong data dataframe=========================\n")
print(dataset)

""" correcting replace wrong data in this dataset duration have a wrong data """
# dataset.loc[7,'Duration'] = 45
# print("\n =======================corrected  dataframe=========================\n")
# print(dataset)
'''For small data sets you might be able to replace the wrong data one by one, but not for big data sets.'''

'''To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.'''

for x in dataset.index:
    if dataset.loc[x,"Duration"] > 120:
        dataset.loc[x,"Duration"] = 120
print(dataset.to_string())