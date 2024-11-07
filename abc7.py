import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform

# Function to compute the distance matrix
def compute_distance_matrix(data):
    return squareform(pdist(data.reshape(-1, 1), metric='euclidean'))

# Function to print matrix with headers
def print_distance_matrix(matrix, labels):
    df = pd.DataFrame(matrix, index=labels, columns=labels)
    print(df)

# Single linkage method: find the closest pair and merge clusters
def single_linkage_clustering(data_points):
    # Step 1: Sort data points
    sorted_data = np.sort(np.array(data_points))
    print("Sorted Data Points:")
    print(sorted_data)

    # Step 2: Compute initial distance matrix
    distance_matrix = compute_distance_matrix(sorted_data)
    labels = list(sorted_data)
    print("\nInitial Distance Matrix:")
    print_distance_matrix(distance_matrix, labels)

    # Step 3: Start clustering process
    cluster_steps = []
    while len(distance_matrix) > 1:
        # Find the minimum distance (excluding diagonal 0s)
        min_distance = np.inf
        min_i, min_j = -1, -1
        for i in range(len(distance_matrix)):
            for j in range(i + 1, len(distance_matrix)):
                if distance_matrix[i, j] < min_distance:
                    min_distance = distance_matrix[i, j]
                    min_i, min_j = i, j

        # Merge clusters i and j
        print(f"\nCombining {labels[min_i]} and {labels[min_j]} with minimum distance {min_distance:.2f}")

        # Step 4: Update the distance matrix using the single linkage rule
        new_row = np.minimum(distance_matrix[min_i], distance_matrix[min_j])
        
        # Remove the rows and columns of the merged clusters
        distance_matrix = np.delete(distance_matrix, [min_i, min_j], axis=0)
        distance_matrix = np.delete(distance_matrix, [min_i, min_j], axis=1)
        
        # Add the new row for the merged cluster
        new_row = np.delete(new_row, [min_i, min_j])
        distance_matrix = np.vstack([distance_matrix, new_row])
        
        # New column for the merged cluster
        new_column = np.append(new_row, [0])
        distance_matrix = np.column_stack([distance_matrix, new_column])
        
        # Combine the labels
        new_label = f"({labels[min_i]},{labels[min_j]})"
        labels.pop(max(min_i, min_j))  # Remove the larger index first to avoid shifting
        labels.pop(min(min_i, min_j))
        labels.append(new_label)

        # Print the updated distance matrix at each step
        print("\nUpdated Distance Matrix:")
        print_distance_matrix(distance_matrix, labels)

        # Store the step for dendrogram plotting
        cluster_steps.append([min_i, min_j, min_distance, len(labels)])

    print("\nFinal Cluster:")
    print(labels[0])

    # Step 5: Plot the dendrogram using the steps
    plt.figure(figsize=(10, 7))
    Z = linkage(np.array(data_points).reshape(-1, 1), method='single')
    dendrogram(Z, labels=[str(x) for x in data_points], leaf_font_size=12, distance_sort='ascending', show_leaf_counts=True)
    plt.title("Dendrogram for Single Linkage Clustering")
    plt.xlabel("Data Points")
    plt.ylabel("Euclidean Distance")
    plt.show()

# Taking input
data_points = [int(x) for x in input("Enter data points separated by space: ").split()]

# Run single linkage clustering
single_linkage_clustering(data_points)
