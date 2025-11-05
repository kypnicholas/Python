
import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})

print(df)
print(df.dropna())          # Drop rows with any NaN values. Default is axis=0 (rows)
print(df.dropna(axis=1))    # Drop columns with any NaN values

print(df.dropna(thresh=2))  # Drop rows with less than 2 non-NaN values

print(df.fillna(value='FILL VALUE'))  # Fill NaN values with a specified value
print(df['A'].fillna(value=df['A'].mean()))  # Fill NaN values with the mean of the column