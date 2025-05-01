# Import Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Load the Data set
df = pd.read_csv(r"E:\AIMDP(Module 1)\AIML MODULE\Live_20210128.csv")
df

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

#Exploratory data analysis
#Check shape of the dataset
df.shape

#Preview the dataset
df.head()

#View summary of dataset
df.info()

#Check for missing values in dataset
df.isnull().sum()

#Drop redundant columns
df.drop(['Column1', 'Column2', 'Column3', 'Column4'], axis=1, inplace=True)
df.isnull().sum()

#statistical summary
df.describe()

#Again view summary of dataset
df.info()

# preview of the dataset
df.head()

#Explore status_id, stautus_type, status_published  variable

# view the labels in the variable
df['status_id'].unique()
df['status_type'].unique()
df['status_published'].unique()
# view how many different types of variables are there
len(df['status_id'].unique())
len(df['status_type'].unique())
len(df['status_published'].unique())

# from the above exploration we have found that status_id and status_published have many unique instances , 
#but status_type have 4 different categories
#so we will drop the other variables(status_id and status_published)
df.drop(['status_id', 'status_published'], axis=1, inplace=True)


#declaring feature vector and target variable
x = df
y = df['status_type']


#converting categorical into numerical data by  label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
x['status_type'] = le.fit_transform(x['status_type'])
y = le.transform(y)


# summary  and preview of x
x.info()
x.head()

#Min-Max Scaling
cols = x.columns
from sklearn.preprocessing import MinMaxScale
ms = MinMaxScaler()
x= ms.fit_transform(x)
x= pd.DataFrame(x, columns=[cols])
x.head()


#Kmeans model with two clusters - K=2
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0) 
kmeans.fit(x)

#k-means parameter #fixing the centroid
kmeans.cluster_centers_

#finding inertia
kmeans.inertia_

#Check quality of  classification  by the model
labels = kmeans.labels_

# check how many of the samples were correctly labeled
correct_labels = sum(y == labels)
print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))

#Performance metrics- Accuracy 
print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))

#Use elbow method to find optimal number of clusters
from sklearn.cluster import KMeans
cs = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    cs.append(kmeans.inertia_)
plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('CS')
plt.show()

#By the above plot, we can see that there is a kink at k=2. Hence k=2 can be considered a good number of the cluster to cluster this data.
#But, we have seen that I have achieved a weak classification accuracy of 1% with k=2.it is aweakly classified data wity an accuracy of 1%


# Apply KMeans (Plot is by Stand Scaling)
kmeans = KMeans(n_clusters=2, random_state=42)  # Adjust number of clusters as needed
kmeans.fit(X_scaled)
labels = kmeans.labels_
# Plot the clustered scatter plot (Using just two features for 2D visualization)
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', s=50)  # Using first two features for 2D plot
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=200, c='red', marker='x', label='Centroids')
plt.title('K-Means Clustering ')
plt.xlabel('Feature 1 ')
plt.ylabel('Feature 2 ')
plt.legend()
plt.grid(True)
plt.show()



#Kmeans model with three clusters - K=3
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=0) 
kmeans.fit(x)
kmeans.cluster_centers_
kmeans.inertia_
labels = kmeans.labels_
correct_labels = sum(y == labels)
print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))
print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))

# Apply KMeans (Plot is by Stand Scaling)
kmeans = KMeans(n_clusters=3, random_state=42)  # Adjust number of clusters as needed
kmeans.fit(X_scaled)
labels = kmeans.labels_
# Plot the clustered scatter plot (Using just two features for 2D visualization)
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', s=50)  # Using first two features for 2D plot
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=200, c='red', marker='x', label='Centroids')
plt.title('K-Means Clustering ')
plt.xlabel('Feature 1 ')
plt.ylabel('Feature 2 ')
plt.legend()
plt.grid(True)
plt.show()

#Kmeans model with four clusters - K=4
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, random_state=0) 
kmeans.fit(x)
kmeans.cluster_centers_
kmeans.inertia_
labels = kmeans.labels_
correct_labels = sum(y == labels)
print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))
print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))

# Apply KMeans (Plot is by Stand Scaling)
kmeans = KMeans(n_clusters=4, random_state=42)  # Adjust number of clusters as needed
kmeans.fit(X_scaled)
labels = kmeans.labels_
# Plot the clustered scatter plot (Using just two features for 2D visualization)
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', s=50)  # Using first two features for 2D plot
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=200, c='red', marker='x', label='Centroids')
plt.title('K-Means Clustering ')
plt.xlabel('Feature 1 ')
plt.ylabel('Feature 2 ')
plt.legend()
plt.grid(True)
plt.show()


