
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')         # Load the tips dataset (built in data set in seaborn)
#print(tips.head())                             # Display the first 5 rows of the dataset
tips.head()

# DISPLOT  
# Univariate distribution plot. It shows the distribution of a single variable. (PLEASE NOTE DISTPLOT IS A DEPRECATED FUNCTION)
# It combines a histogram and a kernel density estimate (KDE) plot.
# BINS are the intervals into which the data is divided. 

sns.displot(tips['total_bill'])
sns.displot(tips['total_bill'], kde= False, bins=30)  # Histogram with 30 bins
plt.show()


# JOINTPLOT
# Bivariate distribution plot. It shows the relationship between two variables.
# With your choice of what kind parameter to compare with: scatter, hex, kde, or hist.

sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')  # Variable 1, Variable 2, Data, Kind of plot
plt.show()

sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
plt.show()


# PAIRPLOT
# Multivariate distribution plot. It shows the relationship between multiple variables. 
# It will create a JOINTPLOT for each pair of (numerical) variables in the dataset.
# It creates a grid of subplots, where each subplot shows the relationship between two variables.
# The diagonal subplots show the distribution of each variable.

sns.pairplot(tips)
plt.show()

# hye argument is used to specify the hue variable.
# This is the column name of a categorical variable (a variable with a limited number of values like Gender/ Sex) in the dataset.

sns.pairplot(tips,hue='sex',palette='coolwarm')
plt.show()


# RUGPLOT
# A rug plot is a simple way to visualize the distribution of a single variable.
# They are the building block of a KDE (Kernel Density Estimation) plot

sns.rugplot(tips['total_bill'])
plt.show()


# KDEPLOT
# A kernel density estimate (KDE) plot is a smoothed version of a histogram.
# It shows the probability density function of a continuous variable.
# It is a way to visualize the distribution of a single variable.

sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])
plt.show()
