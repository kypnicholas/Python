import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

USAhousing = pd.read_csv(r"C:\Users\nkypri01\Downloads\LEARN\Python\MyPythonExercises\Python_DS_ML\USA_Housing.xls")
print(USAhousing.head())

# USAhousing.info()                   # Get a concise summary of the DataFrame
# print(USAhousing.describe())        # Generate descriptive statistics

'''
sns.pairplot(USAhousing)           # Pairwise relationships in the dataset
plt.show()  
'''

# Distribution plot for the 'Price' column
sns.displot(USAhousing['Price'])   
# plt.show()

# Correlation heatmap for numerical features. 
# If we do not specify include=[np.number], it will throw error due to non-numeric columns.
sns.heatmap(USAhousing.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')       
# plt.show()


### Preparing data for Linear Regression model
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                'Avg. Area Number of Bedrooms', 'Area Population']]                             # FEATURES
y = USAhousing['Price']                                                                         # TARGET VARIABLE


### Splitting the dataset into training and testing sets
from sklearn.model_selection import train_test_split                                                 # Importing the train_test_split function
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)           # Splitting the data: 60% training, 40% testing. Random state for reproducibility.

### Training the Linear Regression model
from sklearn.linear_model import LinearRegression                                                    # Importing the Linear Regression model
lm = LinearRegression()                                                                              # Creating an instance of the model
lm.fit(X_train, y_train)                                                                             # Fitting the model to the training data

### Model evaluation
# Coefficients represent the weights assigned to each input feature. They indicate how much each feature contributes to the prediction.
print("Coefficients: \n", lm.coef_)                                                                  # Displaying the coefficients of the model
print("Intercept: \n", lm.intercept_)                                                                # Displaying the intercept of the model

coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])                                  # Creating a DataFrame to display feature names and their corresponding coefficients
print(coeff_df)

### Making predictions using the trained model
predictions = lm.predict(X_test)                                                                      # Making predictions on the test set
plt.scatter(y_test,predictions)                                                                       # Scatter plot of actual vs predicted values
plt.xlabel('Y Test (True Values)')
plt.ylabel('Predictions')       
plt.show()

# Residuals (the differences between actual and predicted values from a model). 
# Should be normally distributed if the model is a good fit.
sns.displot((y_test - predictions), bins=50)                                                         # Distribution of residuals. 
plt.show()

### Calculating evaluation metrics
from sklearn import metrics
print("MAE: ", metrics.mean_absolute_error(y_test, predictions))                                     # Mean Absolute Error (MAE)
print("MSE: ", metrics.mean_squared_error(y_test, predictions))                                     # Mean Squared Error (MSE)
print("RMSE: ", np.sqrt(metrics.mean_squared_error(y_test, predictions)))                            # Root Mean Squared Error (RMSE)