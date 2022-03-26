from statistics import median, stdev
import numpy as np
import pandas as pd

df=pd.read_csv("datascience/names_ages.csv")
# print(df)
# print(df["Age"])
marray=pd.array(df["Age"])
mean_=np.mean(marray)
median_=np.median(marray)
stddev=np.std(marray)

print("The mean of the ages is:",mean_)
print("The median of the ages is:",median_)
print("The standard deviation of the ages is:",stddev)
# print("Ages within one standard deviation are:")