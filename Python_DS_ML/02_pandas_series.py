
# Pandas Series
# class pandas.Series(data=None, index=None, dtype=None, name=None, copy=None, fastpath=<no_default>)

import numpy as np
import pandas as pd

labels = ['a','b','c']              # List of strings
my_list = [10,20,30]                # List of integers
arr = np.array([10,20,30])          # Numpy array 
d = {'a':10,'b':20,'c':30}          # Dictionary

print(pd.Series(data=my_list))                      # Creating a series from a list (returns the index in a numeric format)
print(pd.Series(data=my_list, index=labels))        # Creating a series from a list (returnes a labeled index in an alphabetical format) 
print(pd.Series(my_list, labels))                   # same output as above since the parameters are passed in the same order. 

print(pd.Series(arr))                              # Creating a series from a numpy array
print(pd.Series(arr, labels))                      # Creating a series from a numpy array with labeled index
print(pd.Series(d))                                # Creating a series from a dictionary - it automatically uses the keys as the index!! 


# A pandas Series can hold a variety of object types
print(pd.Series(data=labels))                      # Creating a series from a list of strings
print(pd.Series(data=[sum,print,len]))              # Creating a series from a function (rarely used)

# Creating a series from a dictionary with a custom index
ser1 = pd.Series(['USA', 'Germany','USSR','Japan'],[1,2,3,4])
print(ser1)
print(ser1[1])                                  # Accessing an element in the series by index


# Operations with Series 
# OPERATIONS ARE DONE BASED OFF THE INDEX
ser1 = pd.Series([1,2,3,4],['USA', 'Germany','USSR','Japan'])
ser2 = pd.Series([1,2,5,4],['USA', 'Germany','Italy','Japan'])

print(ser1 + ser2)                                # Adding two series element-wise (returns a new series)