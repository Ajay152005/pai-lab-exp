import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

np.random.seed(42)
data_points = np.random.rand(100, 2) * 10

k = int(input("Enter the number of clusters: "))

kmeans = KMeans(n_clusters=k)
kmeans.fit(data_points)

labels = kmeans.labels_

centroids = kmeans.cluster_centers_

plt.scatter(data_points[:, 0], data_points[:, 1], c = labels, cmap='viridis', alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='gold', marker='x', s=200)
plt.title(f"K-Means Clustering (k = {k})")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

