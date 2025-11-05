
import seaborn as sns  
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

## LMPLOT ##
# A linear model plot is a scatter plot with a regression line fitted to the data.

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm', markers=['o','v'])    # Scatter plot with regression line
plt.title('Total Bill vs Tip with Regression Line')                                                 # Add a title to the plot
# plt.show()  


# Using a grid # 
# We can add more variable separation through columns and rows with the use of a grid. Just indicate this with the col or row arguments:
# NOTE THAT INSTEAD OF SEPARATING THE DATA BY HUE, WE ARE NOW SEPARATING THE DATA BY COLUMNS OR ROWS !!

sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')
plt.show()

sns.lmplot(x="total_bill", y="tip", row="sex", col="time",data=tips)
plt.show()
