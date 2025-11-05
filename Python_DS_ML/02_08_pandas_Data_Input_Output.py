
import numpy as np
import pandas as pd

## Please ensure that the files are in the same directory as your working directory or provide the full path to the files.
## To check your working directory, use the following command: 'pwd' in the terminal or 'os.getcwd()' in Python.


## READING AND WRITING DATA
# 1. Read CSV file 

df = pd.read_csv('example')
print(df)                      # Reading a CSV file into a DataFrame

print(df.to_csv('new') )                # Writing a DataFrame to a CSV file. The index is included by default as a COLUMN.
print(df.to_csv('new', index=False))    # Writing a DataFrame to a CSV file without the index

# 2. Read Excel file
df = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')    # Reading an Excel file into a DataFrame. The default sheet is the first one.
print(df)                      # Reading an Excel file into a DataFrame

print(df.to_excel('new.xlsx', sheet_name='Sheet1'))    # Writing a DataFrame to an Excel file. The index is included by default as a COLUMN.
#print(df.to_excel('new.xlsx', sheet_name='Sheet1', index=False))    # Writing a DataFrame to an Excel file without the index


# 3. Read HTML file

df = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')    # Reading an HTML file into a DataFrame. The default sheet is the first one.
print(df)                      # Reading an HTML file into a DataFrame
print(df[0])                  # Reading the first table in the HTML file into a DataFrame


# 4. Read SQL file
## See jupyter notebook for more details on how to read SQL files into a DataFrame.