import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1',index_col=0)
df2 = pd.read_csv('df2')

#print(df1.head())
#print(df2.head())
'''
plt.style.use('bmh')
df1['A'].hist() # Use bmh style for the plot
plt.show()

plt.style.use('dark_background')
df1['A'].hist()
plt.show()

plt.style.use('ggplot') # Use ggplot style for the plot
df1['A'].hist()
plt.show()


## PLOT TYPES ## 

# AREA PLOT # 
df2.plot.area(alpha=0.4)  # alpha controls the transparency
plt.show()

# BAR PLOT #
df2.plot.bar()  # Default is vertical bar plot
df2.plot.bar(stacked=True)  # Stacked bar plot
plt.show()

# HISTOGRAM #
df2['A'].plot.hist(bins=50, alpha=0.5)  # Histogram with 50 bins and 50% transparency
plt.show()

# LINE PLOT #
df1.plot.line(y='B',figsize=(12,3),lw=1)
plt.show()

# SCATTER PLOT #
df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')  
plt.show()

# BOX PLOT #
df2.plot.box()
plt.show()
'''

# HEXBIN PLOT #

df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])     # New DataFrame with 1000 rows and 2 columns
df.plot.hexbin(x='a',y='b',gridsize=25,cmap='Oranges')
plt.show()


# KDE PLOT #
df2['a'].plot.kde()  # Kernel Density Estimate plot for column 'a'
plt.show()

df2.plot.density()
plt.show()