import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/rpart/kyphosis.csv', index_col=0)
print(df.head())

sns.pairplot(df,hue='Kyphosis',palette='Set1')
plt.show()


### TRAIN TEST SPLIT ###
X = df.drop('Kyphosis', axis=1)          # FEATURES
y = df['Kyphosis']                       # TARGET VARIABLE
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=101)   # Splitting the data: 70% training, 30% testing

from sklearn.tree import DecisionTreeClassifier 
dtree = DecisionTreeClassifier()                    # Creating an instance of the Decision Tree Classifier
dtree.fit(X_train, y_train)                         # Fitting the model to the training data    
predictions = dtree.predict(X_test)                 # Making predictions on the test set

### EVALUATION ###
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, predictions))            # Displaying the confusion matrix
print(classification_report(y_test, predictions))       # Displaying the classification report  


### RANDOM FOREST CLASSIFIER ###
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=200)        # Creating an instance of the Random Forest Classifier with 200 trees
rfc.fit(X_train, y_train)                             # Fitting the model to the training data
rfc_predictions = rfc.predict(X_test)                 # Making predictions on the test set
print(confusion_matrix(y_test, rfc_predictions))          # Displaying the confusion matrix
print(classification_report(y_test, rfc_predictions))     # Displaying the classification report

