import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

#print(cancer.keys())                    # Display the keys of the cancer dataset
#print(cancer['DESCR'])                  # Display the full description of the dataset   

df_feat = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])   # Create a DataFrame with the feature data
print(df_feat.head())                       


### TRAIN TEST SPLIT ###
from sklearn.model_selection import train_test_split
X = df_feat                                         # FEATURES
y = cancer['target']                               # TARGET VARIABLE
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=101)   # Splitting the data: 70% training, 30% testing

### TRAIN THE MODEL ###
from sklearn.svm import SVC
model = SVC()                                       # Creating an instance of the Support Vector Classifier
model.fit(X_train, y_train)                         # Fitting the model to the training data

### PREDICTIONS AND EVALUATION ###
predictions = model.predict(X_test)                 # Making predictions on the test set
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, predictions))            # Displaying the confusion matrix
print(classification_report(y_test, predictions))       # Displaying the classification report

### HYPERPARAMETER TUNING ###
# In some cases, the default parameters of the SVC model may not yield the best performance. e.g. classify everything as 'not cancer' if the data is imbalanced.
# Finding the best parameters for the SVC model using GridSearchCV

from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']}       # Defining the parameter grid to search. Focusing on parameters C and gamma.
grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=3)                                              # Creating an instance of GridSearchCV
grid.fit(X_train,y_train)                                                                               # Fitting the grid search to the training data
print('Best Parameters found: ')
print(grid.best_params_)                                                                                # Displaying the best parameters found by GridSearchCV
print('Best Estimator found: ')
print(grid.best_estimator_)                                                                             # Displaying the best estimator found by GridSearchCV

# Making predictions using the best estimator found by GridSearchCV
grid_predictions = grid.predict(X_test)                     # Making predictions on the test set    
print(confusion_matrix(y_test,grid_predictions))            # Displaying the confusion matrix
print(classification_report(y_test,grid_predictions))       # Displaying the classification report