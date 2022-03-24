import pandas as pd
#the two primary components of pandas are series and dataframes
#series is simply a column
#a dataframe is a multidimensional table made up of a collection of data frames
#a series can be thought of as a one dimensional array while a dataframe as a multidimensional array
#We can create data frames using Dictionaries..
data={
    "age" :[14,18,24,42],
    "height" :[165,180,176,184]
}
#pass the data to a datafram constructor
df=pd.DataFrame(data)
#the dataframe automatically creates a numeric index for each row-
#we can ecplicitly assign indices to the rows
df2=pd.DataFrame(data, index=['Dedan','Wamalwa','Odongo','John'])
#we can then access the rows using the loc[] function
print(df2.loc['Dedan'])