
import numpy as np
import pandas as pd

## Multi-Index and Index Hierarchy

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))          # zip() creates a list of tuples from two lists. 
print(hier_index)

hier_index = pd.MultiIndex.from_tuples(hier_index)      # Creating a multi-level index
print(hier_index)

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])    # Creating a DataFrame with a multi-level index
print(df)

print(df.loc['G1']) # Grabbing a subset of the DataFrame using the outer index
print(df.loc['G1'].loc[1]) # Grabbing a subset of the DataFrame using the outer and inner index


df.index.names = ['Group','Num']    # Naming the index levels
print(df)


# Cross-section
# Cross-section is a way to grab rows or columns from a multi-level index
print(df.xs('G1'))      # Cross-section of the DataFrame using the outer index
print(df.xs(1,level='Num'))  # Cross-section of the DataFrame using the inner index
