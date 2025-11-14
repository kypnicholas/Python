import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the Classified data from a URL
df = pd.read_csv(r'C:\Users\nkypri01\Downloads\LEARN\Python\MyPythonExercises\Python_DS_ML\Classified Data.csv', index_col=0)
print(df.head())

### Standardize the feature variables (all columns except 'TARGET CLASS' that is not classified)
### Standardization ensures that each feature contributes equally to the distance calculations in KNN.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()                                                       # Create an instance of the StandardScaler
scaler.fit(df.drop('TARGET CLASS', axis=1))                                     # Fit the scaler to the feature data                    
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))             # Transform the feature data

print(scaled_features)                                                          # Display the scaled features

# Create a new DataFrame with the scaled features
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])                # Create a DataFrame with scaled features (get every column except the last one)
#print(df_feat.head())                                                           # Display the first few rows of the new DataFrame


# Train-Test Split
from sklearn.model_selection import train_test_split
X = df_feat                                                                                 # FEATURES
y = df['TARGET CLASS']                                                                      # TARGET VARIABLE
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)  # Split the data: 70% training, 30% testing


### K-NEAREST NEIGHBORS (KNN) MODEL ###
from sklearn.neighbors import KNeighborsClassifier  
knn = KNeighborsClassifier(n_neighbors=1)                       # Create an instance of the KNN classifier with k=1 
knn.fit(X_train, y_train)                                       # Fit the model to the training data
predictions = knn.predict(X_test)                               # Make predictions on the test set
#print(predictions)                                              # Display the predictions


### Evaluating the model ###
from sklearn.metrics import classification_report, confusion_matrix
print('WITH K=1')
print('\n')
print(confusion_matrix(y_test, predictions))                            # Display the confusion matrix
print(classification_report(y_test, predictions))                       # Display the classification report


### Choosing the optimal value of K ###
error_rate = []                                                        # Create an empty list to store error rates

for i in range(1, 40):                                               # Loop through K values from 1 to 39
    knn = KNeighborsClassifier(n_neighbors=i)                           # Create a KNN classifier with the current K value
    knn.fit(X_train, y_train)                                         # Fit the model to the training data
    pred_i = knn.predict(X_test)                                      # Make predictions on the test set
    error_rate.append(np.mean(pred_i != y_test))                      # Calculate and store the error rate

# Plot the error rates vs K values
plt.figure(figsize=(10,6))                                                                                                  # Set the figure size
plt.plot(range(1,40), error_rate, color='blue', linestyle='dashed', marker='o',markerfacecolor='red', markersize=10)        # Plot the error rates
plt.title('Error Rate vs. K Value')                                                                                         # Add a title to the plot
plt.xlabel('K')                                                                                                             # Label the x-axis
plt.ylabel('Error Rate')                                                                                                    # Label the y-axis
plt.show()                                                                                                                  # Display the plot

## The results show that the error rate is the lowest when K=17.
## Let's retrain the model using K=17 and evaluate its performance again.

knn = KNeighborsClassifier(n_neighbors=17)                    # Create a KNN classifier with k=17
knn.fit(X_train, y_train)                                     # Fit the model to the training data
predictions = knn.predict(X_test)                            # Make predictions on the test set 
print('WITH K=17')
print('\n')
print(confusion_matrix(y_test, predictions))                  # Display the confusion matrix
print(classification_report(y_test, predictions))             # Display the classification report
# The model performance has improved with the optimal K value.