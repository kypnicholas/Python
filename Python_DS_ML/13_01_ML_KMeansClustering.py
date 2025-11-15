import seaborn as sns
import matplotlib.pyplot as plt

### CREATE SYNTHETIC DATA ###
from sklearn.datasets import make_blobs                                                             # Import make_blobs to create synthetic data
data = make_blobs(n_samples=200, n_features=2,centers=4, cluster_std=1.8,random_state=101)          # Create synthetic data with 200 samples, 2 features, and 4 centers

### VISUALIZE THE DATA ###
# data[0] a 2D array of shape (200, 2) containing the coordinates of 200 points.
# data[0][:,0] is the first feature (x-axis)
# data[0][:,1] is the second feature (y-axis)
# data[1] contains the cluster labels for each data point.Sets the color of each point based on its cluster label.
# cmap='rainbow' sets the color map to 'rainbow'.
plt.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')                                         # Scatter plot of the synthetic data.
plt.show()


### CREATING THE CLUSTERS ###
from sklearn.cluster import KMeans                                                                    # Import KMeans clustering algorithm
kmeans = KMeans(n_clusters=4)                                                                          # Create an instance of KMeans with 4 clusters
kmeans.fit(data[0])                                                                                    # Fit the model to the synthetic data
clusters = kmeans.cluster_centers_                                                                     # Get the coordinates of the cluster centers
labels = kmeans.labels_                                                                                # Get the labels assigned to each data point
print('Cluster Centers: \n', clusters)                                                                # Display the cluster centers
print('Labels: \n', labels)                                                                           # Display the labels

### VISUALIZING THE CLUSTERS ###
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))                                        # Create a figure with two subplots side by side    
ax1.set_title('K Means')
ax1.scatter(data[0][:,0],data[0][:,1],c=kmeans.labels_,cmap='rainbow')  
ax2.set_title("Original")
ax2.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')
plt.show()