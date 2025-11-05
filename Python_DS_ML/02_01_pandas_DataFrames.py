
# DataFrames are the workhorse of pandas and are directly inspired by the R programming language.
# We can think of a DataFrame as a bunch of Series objects put together to share the same index.

import numpy as np
import pandas as pd

np.random.seed(101)     # Setting a seed for reproducibility    

## Creating a DataFrame with random numbers 
df = pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

## Selecting a COLUMN from the DataFrame
print(df['W'])          # Returns a pandas Series
print(df[['W','Z']])    # Returns a DataFrame

## Adding a new column to the DataFrame  
df['new'] = df['W'] + df['Y']       # The new column is the sum of columns W and Y
print(df)

## Removing a column from the DataFrame
print(df.drop('new', axis=1))                       # NOT INPLACE. This drop method does not change the original DataFrame    
print(df.drop('new', axis=1, inplace=True))         # INPLACE. This drop method changes the original DataFrame

## Removing a row from the DataFrame
print(df.drop('E', axis=0))                          # NOT INPLACE. This drop method does not change the original DataFrame
# print(df.drop('E', axis=0, inplace=True))            # INPLACE. This drop method changes the original DataFrame

## Selecting a ROW from the DataFrame
print(df.loc['A'])          # Returns a row (pandas Series) based on a location
print(df.iloc[0])           # Returns a row (pandas Series) based on an INDEX location.


print(df)
print(df.loc['B','Y'])                  # Accessing an element in a DataFrame
print(df.loc[['A','B'],['W','Y']])      # Selecting multiple rows and columns from the DataFrame
print(df.loc['A':'C','W':'Y'])          # Selecting a range of rows and columns from the DataFrame
print(df.loc[['A','B']])                # Selecting multiple rows from the DataFrame   