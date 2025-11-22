import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Import the breast cancer dataset from sklearn
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()                           # Load the breast cancer dataset into the variable 'cancer'

#print(cancer.keys()) 
#print(cancer['DESCR'])                                  # Print the description of the dataset

# Create a DataFrame with the feature data
df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
print(df.head())                                        

### STANDARDIZE THE DATA ###
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()                               # Create an instance of StandardScaler
scaler.fit(df)                                         # Fit the scaler to the DataFrame
scaled_data = scaler.transform(df)                     # Transform the DataFrame to standardized data
print('scaled_data:')
print(scaled_data)                                      # Print the standardized data

### PCA ###
from sklearn.decomposition import PCA
pca = PCA(n_components=2)                              # Create an instance of PCA to reduce the data to 2 components
pca.fit(scaled_data)                                   # Fit PCA to the standardized data
x_pca = pca.transform(scaled_data)                     # Transform the standardized data to its PCA representation
print('scaled_data:')
print(scaled_data.shape)                               # Print the shape of the standardized data
print('x_pca:')
print(x_pca.shape)                                     # Print the shape of the PCA transformed data
## GREAT !! WE REDUCED THE DATA FROM 30 DIMENSIONS TO 2 DIMENSIONS ##


## VISUALIZE PCA DATA ###
plt.figure(figsize=(8,6))                              # Create a new figure with specified size
plt.scatter(x_pca[:,0], x_pca[:,1], c=cancer['target'], cmap='plasma')  # Scatter plot of the PCA data colored by target variable (i.e., malignant or benign)
plt.xlabel('First Principal Component')                # Label for the x-axis
plt.ylabel('Second Principal Component')               # Label for the y-axis
plt.show()

# PCA COMPONENTS
print('PCA COMPONENTS:')
print(pca.components_)  
# Each row in pca.components_ corresponds to a principal component
# Each column corresponds to the original feature

# Create a DataFrame to visualize the PCA components
df_comp = pd.DataFrame(pca.components_, columns=cancer['feature_names'])
print('PCA COMPONENTS DATAFRAME:')
print(df_comp)
# A heatmap to visualize the PCA components
plt.figure(figsize=(12,6))                              # Create a new figure with specified size
sns.heatmap(df_comp, cmap='plasma')                      # Create a heatmap of the PCA components using the 'plasma' colormap
plt.show()  
# This heatmap shows how much each original feature contributes to each principal component