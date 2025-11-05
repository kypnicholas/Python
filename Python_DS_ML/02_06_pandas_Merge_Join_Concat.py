
import numpy as np
import pandas as pd

# CONCATENATION
# Concatenation is the process of combining two or more DataFrames along a particular axis (rows or columns).
# It is similar to the SQL UNION operation.

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

print(pd.concat([df1, df2, df3]))  # Concatenating DataFrames along rows (axis=0)
print(pd.concat([df1, df2, df3], axis=1))  # Concatenating DataFrames along columns (axis=1)


# MERGE
# Merge is a powerful function that allows you to combine two DataFrames based on a common column or index. 
# It is similar to the SQL JOIN operation.
# It can be used to perform inner, outer, left, and right joins.

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})   

print(pd.merge(left,right,how='inner',on='key'))  # INNER join of 'left' and 'right' dataframes on the 'key' column


left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left, right, on=['key1', 'key2']))                   # Merge on multiple keys. By default, it performs an INNER join.
print(pd.merge(left, right, how='outer', on=['key1', 'key2']))      # OUTER join of 'left' and 'right' dataframes on the 'key1' and 'key2' columns


# JOIN
# Join is a method that allows you to combine two DataFrames based on their indexes.    
# It is similar to the SQL JOIN operation.
# It can be used to perform inner, outer, left, and right joins.

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

print(left.join(right))                 # INNER join of 'left' and 'right' dataframes on the index. By default, it performs an INNER join.
print(left.join(right, how='outer'))    # OUTER join of 'left' and 'right' dataframes on the index.