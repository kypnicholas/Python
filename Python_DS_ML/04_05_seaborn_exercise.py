
import seaborn as sns  
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

print(titanic.head()) 

'''
sns.jointplot(x='fare', y='age', data=titanic, kind='scatter')

sns.displot(titanic['fare'],bins=30,kde=False,color='red')

sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')

sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')
plt.show()
'''

correlation_matrix = titanic.select_dtypes(include=['number']).corr()      # Select ONLY numerical columns and compute correlation

sns.heatmap(correlation_matrix, cmap='coolwarm')  # Add annotations and a colormap
plt.show() 

g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')
plt.show()
