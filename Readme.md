Pandas Tutorial 

Whats i panda ?
 - it is python library 
 - used for working with data set
 - it is a funtion for analyzing ,cleaning,exploring, manipulating data

installation :-

pip install pandas

import pandas as pd


Pandas Series : -
 ->  Pandas Series is like a column in a table
 -> It is a one-dimensional array holding data of any type.

Pandas DataFrames : -
 -> it is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
  
    syntax : -
     * pd.DataFrame(data) *
  Eg ;
  calories  duration
  0       420        50
  1       380        40
  2       390        45

locate values from dataForm :-
use loc() method

* Named Indexes :-

pd.DataFrame(data, index = ["day1", "day2", "day3"])


load a file into  dataFrame :

use read_csv() method 

====================================
CSV 

-> CSV :- way to store big data sets is to use CSV files (comma separated files).


- Check the number of maximum returned rows:
        * print(pd.options.display.max_rows)

- Increase the maximum number of rows to display the entire DataFrame:

pd.options.display.max_rows = 9999

+ Read JSON :-

--> for read a json file use read_json() method 

    pd.read_json('data.json')

+ Pandas - Analyzing DataFrames:-

--> It have some methods for overview of the dataFrame

 1. head()
   -->  The head() method returns the headers and a specified number of rows, starting from the top.
    eg:- dataframevariable.head(3)
    --> if the number of rows is not specified, the head() method will return the top 5 rows.

2. tail()
    -->  tail() method for viewing the last rows of the DataFrame.
    --> it returns the headers and a specified number of rows, starting from the bottom.

3. info()
    --> The DataFrames object has a method called info(), that gives you more information about the data set.
           print(df.info())

* Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data

+ Pandas - Cleaning Data :-
 -> Data cleaning is a fixing bad data in your data set.
- Bad data could be:
    # Empty cells
    # Data in wrong format
    # Wrong data
    # Duplicates

*  Pandas - Cleaning Empty Cells
 
 1. Empty Cells 
    -> empty cell give wrong result  when analyse data

Solutions :-
    1 Remove Rows :-
    - One way to deal with empty cells is to remove rows that contain empty cells.
    - use dropna() method for removing emptycell rows
    - dropna() method returns a new DataFrame, and will not change the original.

    - change original data use inplace argument 
        dropna(inplace = True)
    - dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

    2. Replace Empty Values :-
      
      - dealing with empty cells is to insert a new value instead.
      - This way you do not have to delete entire rows just because of some empty cells.
      - fillna() method allows us to replace empty cells with a value:

      df.fillna(130, inplace = True)
      -  To only replace empty values for one column, specify the column name for the DataFrame:
      df["Calories"].fillna(130, inplace = True)

    3. Replace Using Mean, Median, or Mode:- 
    - Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column

    * Mean()
     - the average value (the sum of all values divided by number of values)
     - df["Calories"].mean()

     * median() : -
      - Median = the value in the middle, after you have sorted all values ascending
      - median_of_data = dataframe["Calories"].median()

      * Mode() :-

       - Mode = the value that appears most frequently.

         mode_of_dataframe = dataframe['Calories'].mode()[0]

* Pandas - Cleaning Data of Wrong Format

- Data of Wrong Format : -
 --> Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
 two solutions : -
 1.  remove the rows
 2. convert all cells in the columns into the same format.

    # dataframe['Date'] = pd.to_datetime(dataframe['Date']) - converting correctformat
    # dataframe.dropna(subset=["Date"],inplace=True) -- row removing

* Fixing Wrong Data

    --> entered wrong values or other in dataset
    --> solution :-
        1. Replacing values 
        2. remove rows 

* Remove duplicate data :- 
    1. duplicated() -check duplicate data exist or not (bool)
    2. drop_duplicates() - remove duplicate datafrom dataframe

* Pandas - Data Correlations:-
    - Finding Relationships
            1. corr() 
                -->   calculates the relationship between each column in your data set.
                --> The corr() method ignores "not numeric" columns.

        eg ; 

                    Duration     Pulse  Maxpulse  Calories
  Duration  1.000000 -0.155408  0.009403  0.922721
  Pulse    -0.155408  1.000000  0.786535  0.025120
  Maxpulse  0.009403  0.786535  1.000000  0.203814
  Calories  0.922721  0.025120  0.203814  1.000000

The number varies from -1 to 1.

1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

'What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.'

* Pandas - Plotting:-
- Pandas uses the plot() method to create diagrams.
- We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.