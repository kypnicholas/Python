import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')


yelp = pd.read_csv('yelp.xls')
print(yelp.head())

# Create a new column called "text length" which is the number of words in the text column.
yelp['text length'] = yelp['text'].apply(len)
print(yelp.head())  

# Use FacetGrid from the seaborn library to create a grid of 5 histograms of text length based off of the star ratings. 
g = sns.FacetGrid(yelp, col='stars')
g.map(plt.hist, 'text length', bins=50)
plt.show()

# Create a boxplot of text length for each star category.
sns.boxplot(x='stars', y='text length', data=yelp, palette='rainbow')
plt.show()

# Create a countplot of the number of occurrences for each type of star rating.
sns.countplot(x='stars', data=yelp, palette='rainbow')
plt.show()  

# Use groupby to get the mean values of the numerical columns:
stars = yelp.groupby('stars').mean(numeric_only=True)               # skip non-numeric columns. numeric_only=True to avoid TypeError. 
print(stars)

# Use seaborn to create a heatmap based off that .corr() dataframe:
sns.heatmap(stars.corr(), annot=True, cmap='coolwarm')
plt.show()

### NLP CLASSIFICATION EXERCISE ###

# Create a dataframe called yelp_class that contains the columns of yelp dataframe but for only the 1 or 5 star reviews.**
yelp_class = yelp[(yelp['stars'] == 1) | (yelp['stars'] == 5)]
print(yelp_class.head())

# Create X and y for the classification task. (Your features and target/labels)
X = yelp_class['text']
y = yelp_class['stars']

# Import CountVectorizer and create a CountVectorizer object.
from sklearn.feature_extraction.text import CountVectorizer 
cv = CountVectorizer()
# Fit and transform the X variable.
X = cv.fit_transform(X)

### TRAIN TEST SPLIT ###
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

### TRAIN A MODEL CLASSIFIER ###
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train, y_train)                                # Fit the model to the training data

### PREDICTIONS AND EVALUATION ###
predictions = nb.predict(X_test)                        # Predict the labels for the test set

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, predictions))            # Confusion matrix
print(classification_report(y_test, predictions))       # Classification report
## the results look very good with high precision and recall for both classes ##

### USING TEXT PROCESSING ###
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('bow', CountVectorizer()),                 # strings to token integer counts
    ('tfidf', TfidfTransformer()),              # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),            # train on TF-IDF vectors w/ Naive Bayes classifier
])

### USING THE PIPELINE ###
### TRAIN TEST SPLIT ###

X = yelp_class['text']
y = yelp_class['stars'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
pipeline.fit(X_train, y_train)                     # Fit the pipeline to the training data

### PREDICTIONS AND EVALUATION ###
predictions = pipeline.predict(X_test)             # Predict the labels for the test set
print(confusion_matrix(y_test, predictions))       # Confusion matrix
print(classification_report(y_test, predictions))  # Classification report

