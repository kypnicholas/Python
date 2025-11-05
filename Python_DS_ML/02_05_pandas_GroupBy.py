
import numpy as np
import pandas as pd

# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

by_comp = df.groupby('Company')             # Group by 'Company' column 
print(by_comp)                              # Returns a DataFrameGroupBy object
print(by_comp.mean(numeric_only=True))      # Ensure only numeric columns are aggregated

print(by_comp.sum())                        # Sum of sales by company  
print(by_comp.std(numeric_only=True))                        # Standard deviation of sales by company
print(by_comp.min())                        # Minimum sales by company
print(by_comp.max())                        # Maximum sales by company
print(by_comp.count())                      # Count of sales by company
print(by_comp.describe())                   # Summary statistics of sales by company
print(by_comp.describe().transpose())       # Transpose the summary statistics for better readability
print(by_comp.describe().transpose()['GOOG']) # Summary statistics for GOOG only
