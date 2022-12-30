import pandas as pd

# dataset = {
#     'cars': ['BMW','audi','benz'],
#     'passing' : [3,7,8]
# }

# mydata = pd.DataFrame(dataset)

# print(mydata)

# print(pd.Series(dataset))
# ================================================================================

# a= [5,6,7]
# data = pd.Series(a)
# print(data[2])

# locating data from dataFrame

dataset = {
    'cars': ['BMW','audi','benz'],
    'passing' : [3,7,8]
}
framdata =pd.DataFrame(dataset)

print(framdata.loc[0])

#use a list of indexes:
print("list of data\n",framdata.loc[[1,2 ]])


# Load Files Into a DataFrame :-
print("\n==============  Load Files Into a DataFrame  =====================\n")
dataframing_file = pd.read_csv('data.csv')
print(dataframing_file)

print("\n==============  Convert dataFrame data to to string  =====================\n")
print(dataframing_file.to_string())


print("\n==============  Check the number of maximum returned rows:  =====================\n")
print(pd.options.display.max_rows)

print("\n==============  Read a Json file  =====================\n")

jsonfile = pd.read_json('data.json')
print(jsonfile.to_string())


print("\n============== Pandas - Analyzing DataFrames  =====================\n")

print(" Viewing the Data :-\n")
print(" 1. head() method :-\n")

print(dataframing_file.head(4))

print(" 2. tail() method :-\n")
print(dataframing_file.tail(2))

print(" 3. info() method :-\n")
print(dataframing_file.info())

# ====== data cleaning ================

# print("\n==================Remove Rows of empty cell=================\n")

# data_with_emptycell = pd.read_csv('data2.csv')

# print(data_with_emptycell)

# removed_empty_cell_data = data_with_emptycell.dropna()

# print("\n==================Remove emptycell row-================== \n")
# print(removed_empty_cell_data.to_string())

print("\n=================Replace Empty Values================== \n")

data_with_emptycell2 = pd.read_csv('data2.csv')
data_with_emptycell2.fillna(130, inplace=True )
print(data_with_emptycell2.to_string())


