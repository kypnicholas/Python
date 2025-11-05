
import seaborn as sns  
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')     # Load the iris dataset
# print(iris.head())


## PAIRGRID ##  
# A PairGrid is a grid of subplots that allows you to visualize pairwise relationships in a dataset.

g = sns.PairGrid(iris, hue='species')   # Create a PairGrid with the iris dataset, colored by species
g.map_diag(plt.hist)                    # Map the diagonal to histograms    
g.map_upper(plt.scatter)                # Map the upper triangle to scatter plots   
g.map_lower(sns.kdeplot)                # Map the lower triangle to kernel density estimates 
g.add_legend()                          # Add a legend to the grid
plt.show()                               


## PAIRPLOT ##
# A PairPlot is a simpler version of PairGrid that automatically creates a grid of scatter plots for each pair of variables.

sns.pairplot(iris, hue='species',palette='rainbow')     # Create a pair plot with the iris dataset, colored by species
plt.show()  


## FACETGRID ##
# A FacetGrid is a grid of subplots that allows you to visualize the distribution of a variable across different categories.

tips = sns.load_dataset('tips')
# print(tips.head())

g = sns.FacetGrid(data=tips, col='time',row='smoker')       # Create AN EMPTY FacetGrid with tips dataset, columns by time and rows by smoker
g = g.map(plt.hist, "total_bill")                           # Map the histogram to the grid 
plt.show()

g = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')    # Create AN EMPTY grid, colored
g = g.map(plt.scatter, "total_bill", "tip")                     # Map the scatter plot to the grid. NOTICE HOW THE ARGS COME AFTER THE plt.scatter FUNCTION
g.add_legend()                                                   # Add a legend to the grid
plt.show()                                                       # Display the plot

