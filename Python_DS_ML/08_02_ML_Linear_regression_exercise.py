'''
PROBLEM STATEMENT:
# An e-commerce company wants to understand the factors that influence their customers' yearly spending.
The company is trying to decide whether to focus their efforts on their mobile app experience or their website. 
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

customers = pd.read_csv(r"C:\Users\nkypri01\Downloads\LEARN\Python\MyPythonExercises\Python_DS_ML\Ecommerce_Customers.csv")
print(customers.head())

# Compare the 'Time on Website' and 'Yearly Amount Spent' columns using a joint plot
sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=customers)   # Joint plot between 'Time on Website' and 'Yearly Amount Spent'
plt.show()

# Compare the 'Time on App' and 'Yearly Amount Spent' columns using a joint plot
sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=customers)       # Joint plot between 'Time on App' and 'Yearly Amount Spent'
plt.show()  

# Hexagonal joint plot to visualize the relationship between 'Time on App' and 'Length of Membership'
sns.jointplot(x='Time on App', y='Length of Membership', kind='hex', data=customers)  # Hexagonal joint plot between 'Time on App' and 'Length of Membership'
plt.show()


# Pair plot 
# to visualize pairwise relationships in the dataset
sns.pairplot(customers)    # Pair plot for the entire dataset   
plt.show()

# Linear model plot 
# to show the relationship between 'Length of Membership' and 'Yearly Amount Spent'
# When you run it you can see that 'Length of Membership' is the feature that is most correlated with 'Yearly Amount Spent'.
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=customers)   # Linear model plot between 'Length of Membership' and 'Yearly Amount Spent'
plt.show()

### Preparing data for Linear Regression model
X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]   # FEATURES
y = customers['Yearly Amount Spent']                                                               # TARGET VARIABLE

### Splitting the dataset into training and testing sets
from sklearn.model_selection import train_test_split                                                 # Importing the train_test_split function
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)       # Splitting the data into training and testing sets


### Training the Linear Regression model
from sklearn.linear_model import LinearRegression                                                    # Importing the Linear Regression model
lm = LinearRegression()                                                                           # Creating an instance of the Linear Regression model
lm.fit(X_train, y_train)                                                                          # Fitting the model to the training data      

### Model evaluation
print("Coefficients: \n", lm.coef_)                                                                  # Displaying the coefficients of

### Visualizing the actual vs predicted values
predictions = lm.predict( X_test)                                                                     # Making predictions on the test set
plt.scatter(y_test,predictions)                                                                       # Scatter plot of actual vs predicted values
plt.xlabel("Actual Yearly Amount Spent")                                                              # Label for x-axis
plt.ylabel("Predicted Yearly Amount Spent")                                                           # Label for y-axis
plt.title("Actual vs Predicted Yearly Amount Spent")                                                  # Title for the plot
plt.show()                                                                                             # Displaying the plot

### EVALUATING THE MODEL
from sklearn import metrics                                                                           # Importing metrics for model evaluation
print('MAE:', metrics.mean_absolute_error(y_test, predictions))                                       # Mean Absolute Error
print('MSE:', metrics.mean_squared_error(y_test, predictions))                                        # Mean Squared Error
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))                              # Root Mean Squared Error 

### Residuals analysis
sns.displot((y_test - predictions), bins=50)                                                         # Distribution plot of residual
plt.show()

'''
We still want to figure out the answer to the original question, do we focus our efforts on mobile app or website development?
'''

# Checking the coefficients to understand the impact of each feature
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])                                  # Creating a DataFrame to display feature names and their corresponding coefficients
print(coeff_df)

'''
Interpreting the coefficients:

Holding all other features fixed, a 1 unit increase in Avg. Session Length is associated with an    increase of 25.98 total dollars spent.
Holding all other features fixed, a 1 unit increase in Time on App is associated with an            increase of 38.59 total dollars spent.
Holding all other features fixed, a 1 unit increase in Time on Website is associated with an        increase of 0.19 total dollars spent.
Holding all other features fixed, a 1 unit increase in Length of Membership is associated with an   increase of 61.27 total dollars spent.

The company should focus more on their mobile app experience since the coefficient for 'Time on App' is significantly higher than that for 'Time on Website'.
HOWEVER, this is a simplistic analysis and other factors should also be considered before making a final decision.
there are two ways to think about this: Develop the Website to catch up to the performance of the mobile app, or develop the app more since that is what is working better. 
this requires deeper analysis and understanding of the business context.
'''