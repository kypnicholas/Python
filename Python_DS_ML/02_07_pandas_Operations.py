
import numpy as np
import pandas as pd

import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})


print(df.head())        ## shows the first 5 rows of the DataFrame
print(df.tail())        ## shows the last 5 rows of the DataFrame

print(df['col2'].unique())          ## shows AN ARRAY with the unique values in the column col2
print(df['col2'].nunique())         ## shows the number of unique values in the column col2 
print(df['col2'].value_counts())    ## shows the number of times each unique value appears in the column col2.

newdf = df[(df['col1']>2) & (df['col2']==444)]      ## #Select from DataFrame using criteria from multiple columns
print(newdf)            


## APPLY() function to DataFrame
def times2(x):
    return x*2

print(df['col1'].apply(times2))         ## Apply a CUSTOM function to a column in the DataFrame. This will return a Series with the results.
print(df['col3'].apply(len))            ## Apply a BUILT-IN function to a column in the DataFrame. This will return a Series with the results.
print(df['col2'].apply(lambda x: x*2))  ## Apply a LAMBDA function to a column in the DataFrame. This will return a Series with the results.


print(df.columns)         ## shows the column names of the DataFrame
print(df.index)           ## shows the index of the DataFrame

print()
print(df.sort_values('col2'))         ## Sort by a column.  inplace=False by default 
print(df.sort_values('col2', ascending=False))         ## Sort by a column in descending order.  inplace=False by default

print(df.isnull)        ##  Will return a DataFrame with True or False values indicating whether each value is null or not.


## Creating a PIVOT table

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)

print(df.pivot_table(values='D',index=['A','B'],columns=['C']))  ## Creating a pivot table. The values are aggregated by the mean by default.