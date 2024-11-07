import numpy as np
import random

# Function to calculate the Euclidean distance between two points
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# Function to calculate the mean of the clusters
def calculate_mean(clusters, data):
    means = []
    for cluster in clusters:
        means.append(np.mean(data[cluster], axis=0))
    return means

# K-Means algorithm
def k_means(data, k):
    # Convert data to a 2D array if it's not already
    if data.ndim == 1:
        data = data[:, np.newaxis]

    # Step 1: Print elements of the data set
    print("1. Elements of data set:")
    print(data.tolist())

    # Step 2: Cluster size k
    print(f"\n2. Cluster size k={k}")

    # Randomly select initial cluster centroids
    centroids = data[random.sample(range(len(data)), k)]
    clusters = [[] for _ in range(k)]
    iteration = 0

    while True:
        print(f"\nIteration {iteration + 1}:")

        # Step 3: Assign each point to the nearest centroid
        new_clusters = [[] for _ in range(k)]
        for i, point in enumerate(data):
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest_centroid = np.argmin(distances)
            new_clusters[closest_centroid].append(i)

        # Step 4: Calculate the new centroids
        new_centroids = calculate_mean(new_clusters, data)

        # Convert clusters to Python lists for printing
        new_clusters_list = [list(np.array(cluster)) for cluster in new_clusters]
        new_centroids_list = [float(mean[0]) for mean in new_centroids]  # Assuming 1D data

        # Print initial clusters
        if iteration == 0:
            print("\n3. Initial clusters:")
            for i, cluster in enumerate(new_clusters_list):
                print(f"Cluster {i + 1}: {data[cluster].tolist()}")
            print("\nMean of initial clusters:")
            print(new_centroids_list)
        else:
            print("\n4. Other clusters:")
            for i, cluster in enumerate(new_clusters_list):
                print(f"Cluster {i + 1}: {data[cluster].tolist()}")
            print("\nMean of clusters:")
            print(new_centroids_list)

        # Step 5: Check for convergence (if centroids don't change)
        if np.allclose(centroids, new_centroids):
            print("\n5. Clusters have stabilized. Final clusters and means:")
            for i, cluster in enumerate(new_clusters_list):
                print(f"Final Cluster {i + 1}: {data[cluster].tolist()}")
            print("Final Mean of clusters:")
            print(new_centroids_list)
            break

        centroids = new_centroids
        clusters = new_clusters
        iteration += 1

# Example data set
data = np.array([2, 3, 4, 20, 25, 30, 11])
# Number of clusters (k)
k = 2
# Run K-Means algorithm
k_means(data, k)
