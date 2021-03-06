from calendar import month
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
'''print(df2.loc['Dedan'])
print(df2.loc['Wamalwa'])
print(df2.loc['Odongo'])
#we can access the columns(series) using dataframe_name[column_name]
print(df2["age"])
#to access multiple series...(a dataframe)
print(df2[["age","height"]])
#we can use iloc[] to access rows depending on their numerical indices
print("==Iloc==")
print(df2.iloc[0])
print(df2.iloc[1])
print(df2.iloc[:2])
print(df2.iloc[-1])
print(df2.iloc[-2:])'''
print(df2.iloc[0:])
#conditions
print("==conditions==")
# print(df2[(df2["age"]>18) & (df2["height"]>170)])
print(df2[(df2["age"]>18)])
# Reading data
# pandas supports reading data from CSV files(comma separated values), JSON files and SQL DBs
# assume we have a file named names_ages.csv,we can read its data using read_csv method
df3=pd.read_csv("datascience/names_ages.csv")
print(df3[0:])
# we can use the head() function to get the first five rows of the data
# head(n)- it will return the first n rows of the dataframe
# tail returns the last 5 rows of the dataframe by default
# we can also pass n to it to print the last n rows
# print(df3.head())
# print(df3.head(6))
print(df3.head(3))
print(df3.tail())
# info() method gives us essential info about the dataset such as no. of rows,columns and data types
df3.info()
# dropping a column or row
# we use drop('name of column/row' ,axis=1/0,inplace=True )
df3.drop('Country', axis=1,inplace=True)
# df3.drop('Paula',axis=0,inplace=True)
print(df3.head())
# working with data
# creating a column
# creating a month column in our dataframe
month=["January","March","July","December","November","January","May","June","July"]
df3['Month']=month
# alternatively...
location=["NRB","KSM","MMS","MSA","NKR","NRB","NRB","KSM","KSM"]
df3.insert(2,"Location",location,True)
print(df3.head())
# summary statistics of numerical columns
print(df3.describe())
# for a particular column...
print(df3['DoB'].describe())

# grouping
# value_counts() returns how many times a value appears in a dataset / frequency
print("==grouping==")
x= df3['Age'].value_counts()
print(x)
x= df3['DoB'].value_counts()
print(x)
# The groupby() function is used to group our dataset by the given column.
print(df3.groupby('Location')['Age'].sum()) #sum of ages of people grouped in their resp. locations


# small exercise 
df3['new_row']=df3["DoB"]/df3["Age"]
print(df3["new_row"])
print(df3.info())
print(df3[(df3["new_row"]==df3["new_row"].max())])