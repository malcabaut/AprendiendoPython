import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
import numpy as np 
from sklearn.datasets.samples_generator import make_blobs 
np.random.seed(0) 
batch_size = 45 
centers = [[1, 1], [-1, -1], [1, -1]] 
n_clusters = len(centers) 
X, labels_true = make_blobs(n_samples=3000, centers=centers, 
cluster_std=0.7) 
num=3 
fitting = KMeans(n_clusters=num).fit(X) 
prediction=fitting.predict(X) 
plt.figure(1) 
centroids = fitting.cluster_centers_ 
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=170, linewidths=3, 
            color='r', zorder=2) 
plt.scatter(X[:, 0], X[:, 1], c=prediction) 
plt.show() 