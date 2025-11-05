
import numpy as np
import pandas as pd

np.random.seed(101)                                                                 # Setting a seed for reproducibility    
df = pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])     # Creating a DataFrame with random numbers
print(df)

print(df>0)         # Returns a DataFrame of boolean values based on the condition
print(df[df>0])     # Returns a DataFrame with NaN values where the condition is not met

print(df['W']>0)    # Returns a Series of boolean values based on the condition
print(df[df['W']>0]) # Returns a DataFrame where the condition is met. This will NOT RETURN row C since it includes NaN values. 

# Grab all the rows in my dataframe where W is greater than 0
print(df[df['W']>0]) 

print(df[df['W']>0]['Y'])           # Returns a Series of values in column Y where the condition is met.
print(df[df['W']>0][['Y','X']])     # Returns a DataFrame of values in columns Y and X where the condition is met.

# BREAK DOWN TO EXPLAIN. The checks below are returning the same results as above. 
boolser = df['W']>0 
result = df[boolser]
mycols = ['Y','X']
result = result[mycols]


print(df[(df['W']>0) & (df['Y'] > 1)])   # Multiple conditions. Returns a DataFrame where BOTH conditions are met.
print(df[(df['W']>0) | (df['Y'] > 1)])   # Multiple conditions. Returns a DataFrame where EITHER condition is met.


print(df)

## RESET the index
print(df.reset_index())             # Resetting the index. The original index is added as a new column
# print(df.reset_index(drop=True))    # Resetting the index. The original index is NOT added as a new column

## SET a new index
newind = 'CA NY WY OR CO'.split()    # Creating a list of strings. Nice trick to create a new list with multiple strings without typing them all out.
df['States'] = newind                # Adding a new column to the DataFrame
print(df)
print(df.set_index('States'))        # SETTING A NEW INDEX. The original index is removed.