import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset from a URL
train = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(train.head())

# Visualize missing data using a heatmap
# What columns have missing data and how much is missing
# sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# plt.show()

# Count plot for 'Survived' column based on Sex
sns.set_style('whitegrid')          
sns.countplot(x='Survived',hue='Sex',data=train,palette='RdBu_r')
#plt.show()

# Count plot for 'Survived' column based on Pclass (passenger class)
sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')
#plt.show()

# Distribution plot for 'Age' column using SEABORN
sns.displot(train['Age'].dropna(),kde=False,color='darkred',bins=30)
#plt.show()

# Distribution plot for 'Age' column using PANDAS
train['Age'].hist(bins=30,color='darkred',alpha=0.7)
#plt.show()  

# Count for fare column using PANDAS
train['Fare'].hist(color='green',bins=40,figsize=(8,4))
#plt.show()

'''
# Count for fare column using CUFFLINKS
# Note: If you face compatibility issues, consider using matplotlib or seaborn for static plots.
import cufflinks as cf
cf.go_offline()     # Initialize cufflinks for offline use
train['Fare'].iplot(kind='hist', bins=40, color='green', title='Fare Distribution') 
plt.show()
'''

import plotly.express as px

fig = px.histogram(train, x='Fare', nbins=30, title='Fare Distribution')
#fig.show()



### DATA CLEANING ###
# We want to fill in the missing Age data instead of dropping the rows
# We can see that wealthier passengers (Pclass=1) tend to be older
# So we'll use the average age of each Pclass to fill in the missing Age values

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age

# Apply the impute_age function to fill in missing Age values
train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)       

# Now let's check the heatmap again to see if there are any missing Age values
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#plt.show()

# Drop the Cabin column since it has too many missing values
train.drop('Cabin',axis=1,inplace=True) 
#print(train.head())

# Drop any remaining rows with missing values
train.dropna(inplace=True)

# Final check for missing data
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis') 
#plt.show()


### Converting categorical features to dummy variables (or INDICATOR VARIABLES) ###
# Convert the 'Sex' column to numerical values
sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'],drop_first=True)
print(sex.head())
print(embark.head())

# Concatenate the new dummy variable columns to the original dataframe
train = pd.concat([train,sex,embark],axis=1)
#print(train.head())

# Drop the  original 'Sex', 'Name', 'Ticket', and 'Embarked' columns since we have converted them to numerical values or they add no value.
train.drop(['Sex','Name','Ticket','Embarked','PassengerId'],axis=1,inplace=True)
#print(train.head())

train = pd.concat([train,sex,embark],axis=1)    
print(train.head())



### BUILDING A LOGISTIC REGRESSION MODEL ###

# Split the data into training set and testing set using train_test_split
from sklearn.model_selection import train_test_split
X = train.drop('Survived',axis=1)   # FEATURES
y = train['Survived']                # TARGET VARIABLE

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.30, random_state=101)

## Training and predicting
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)

## Evaluating the model. Create a classification report and confusion matrix
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))