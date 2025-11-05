
import seaborn as sns  
import matplotlib.pyplot as plt

flights = sns.load_dataset('flights')
tips = sns.load_dataset('tips')



## HEATMAP ##
# A heatmap is a graphical representation of data where individual values are represented as colors.

# TIPS TABLE
correlation_matrix = tips.select_dtypes(include=['number']).corr()      # Select ONLY numerical columns and compute correlation
#print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')  # Add annotations and a colormap
plt.show()  # Display the plot


# FLIGHTS TABLE

flights_pivot = flights.pivot_table(values='passengers', index='month', columns='year')  # Create a pivot table to summarize the data
print(flights_pivot)

sns.heatmap(flights_pivot, cmap='YlGnBu')  # Create a heatmap with annotations and a colormap
plt.show()

sns.heatmap(flights_pivot,cmap='magma',linecolor='white',linewidths=1)  # Create a heatmap with a different colormap and line color
plt.show() 



## CLUSTERMAP ##
# A clustermap is a heatmap with hierarchical clustering applied to the rows and columns.
# Please note that the columns and rows are NO LONGER sorted alphabetically, but by the clustering algorithm.

sns.clustermap(flights_pivot, cmap='YlGnBu', standard_scale=1)  # Create a clustermap with standard scaling
plt.show()  # Display the plot