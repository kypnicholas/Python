import numpy as np
import pandas as pd

# Load the dataset that holds user ratings of movies
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('https://files.grouplens.org/datasets/movielens/ml-100k/u.data', sep='\t', names=column_names) #sep='\t' indicates tab-separated values
#print(df.head())                                                     

# Load movie titles
movie_titles = pd.read_csv('https://files.grouplens.org/datasets/movielens/ml-100k/u.item', sep='|', names=['item_id', 'title'], usecols=[0, 1], encoding='latin-1')
#print(movie_titles.head())

# Merge movie titles with the ratings dataframe
df = pd.merge(df, movie_titles, on='item_id')
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# Create a ratings dataframe with average rating for each movie
ratings = pd.DataFrame(df.groupby('title')['rating'].mean().sort_values(ascending=False))
#print(ratings.head())

# Add a 'num of ratings' column to the ratings dataframe
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count()) 
print(ratings.head())

# Visualizations
ratings['num of ratings'].hist(bins=70)               # Histogram of number of ratings  
plt.show()

ratings['rating'].hist(bins=70)                        # Histogram of ratings
plt.show()

sns.jointplot(x='rating', y='num of ratings', data=ratings, alpha=0.5)  # Jointplot of ratings vs number of ratings
plt.show()

# Jointplot with annotations - highlight top 5 movies by number of ratings
g = sns.jointplot(data=ratings, x='rating', y='num of ratings')

# Annotate top 5 movies by number of ratings
for i, row in ratings.nlargest(5, 'num of ratings').iterrows():
    g.ax_joint.annotate(row.name, (row['rating'], row['num of ratings']),
                        textcoords="offset points", xytext=(5,5), ha='left', fontsize=8, color='red')

plt.show()