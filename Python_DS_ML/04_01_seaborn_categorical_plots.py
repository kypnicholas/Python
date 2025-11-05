
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')         # Load the tips dataset (built in data set in seaborn)
tips.head()
#print(tips.head())                      # Display the first 5 rows of the dataset

# BARPLOT
# Visualization of a GROUP BY operation.
# allows you to aggregate the categorical data based off some function (estimator), by default the mean
# ESTIMATOR is the method for statistical data aggregation, allowing for calculating mean, median, and standard deviation directly within visualizations.

sns.barplot(x='sex',y='total_bill',data=tips)                       # estimator is by default the mean
#plt.show()

import numpy as np

sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)      # estimator is set to standard deviation
#plt.show()


# COUNTPLOT
# A count plot is a bar plot where the height of each bar represents the number of occurrences of each category in the dataset.

sns.countplot(x='sex',data=tips)        # Measure how many Males and Females are in the dataset
#plt.show()


# BOXPLOT
# Show the distribution of categorical data based on a five-number summary: 
# minimum, first quartile (Q1), median (Q2), third quartile (Q3), and maximum.

sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')
#plt.show()

# You can compare a day by day total bill, and also compare the total bill of smokers and non-smokers.
sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm")
#plt.show()


# VIOLINPLOT
# A violin plot is a combination of a box plot and a kernel density plot.
# It shows the distribution of the data across different categories.
# It is useful for visualizing the distribution of a continuous variable across different categories.

sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow')
#plt.show()

sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')
#plt.show()

sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',split=True,palette='Set1')
plt.show()


# STRIPLOT
# A strip plot is a scatter plot where one of the variables is categorical.
# It shows the distribution of a categorical variable along with the individual data points.

sns.stripplot(x="day", y="total_bill", data=tips)
plt.show()

# See the density of the data a bit better
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True)  # Jitter adds random noise to the data points to make them more visible.
plt.show()

sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1')
plt.show()



# FACTORPLOT
# The most general form of a categorical plot. It can take in a **kind** parameter to adjust the plot type:

sns.factorplot(x='sex',y='total_bill',data=tips,kind='bar')
plt.show()