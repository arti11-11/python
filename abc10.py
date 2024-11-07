import numpy as np

def calculate_pagerank(adjacency_matrix, num_iterations, teleportation_factor):
    num_nodes = adjacency_matrix.shape[0]
    
    # Initialize PageRank values
    pagerank = np.ones(num_nodes) / num_nodes
    print(f"Iteration 0: {np.round(pagerank, 2)}\n")  # Print initial PageRank values
    
    # Iteratively compute PageRank
    for iteration in range(num_iterations):
        new_pagerank = np.zeros(num_nodes)
        
        for i in range(num_nodes):
            # Find nodes linking to node i
            incoming_links = np.where(adjacency_matrix[:, i] > 0)[0]
            incoming_rank = sum(
                (pagerank[j] / np.sum(adjacency_matrix[j])) * adjacency_matrix[j, i]
                for j in incoming_links if np.sum(adjacency_matrix[j]) > 0
            )  # Avoid division by zero
            
            # Calculate new PageRank with teleportation factor
            new_pagerank[i] = (1 - teleportation_factor) + teleportation_factor * incoming_rank
            # Round down the new PageRank value to 2 decimal places
            new_pagerank[i] = np.floor(new_pagerank[i] * 100) / 100

            # Display the calculation for each node
            incoming_str = " + ".join(
                f"({np.round(pagerank[j], 2)} / {np.round(np.sum(adjacency_matrix[j]), 2)} * {adjacency_matrix[j, i]})"
                for j in incoming_links if np.sum(adjacency_matrix[j]) > 0
            )
            print(f"PR({chr(65 + i)}) = (1 - {teleportation_factor}) + {teleportation_factor} * [{incoming_str}]")

        # Update pagerank with the new values for this iteration
        pagerank = new_pagerank
        print(f"Iteration {iteration + 1}: {np.round(pagerank, 2)}\n")

def main():
    # Input: number of nodes
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    
    # Input: adjacency matrix
    print("Enter the adjacency matrix row by row (use space to separate values):")
    adjacency_matrix = []
    for _ in range(num_nodes):
        row = list(map(float, input().split()))
        # Round down each input value to 2 decimal places
        row = [np.floor(value * 100) / 100 for value in row]
        adjacency_matrix.append(row)
    adjacency_matrix = np.array(adjacency_matrix)
    
    # Input: number of iterations
    num_iterations = int(input("Enter the number of iterations: "))
    
    # Input: teleportation factor
    teleportation_factor = float(input("Enter the teleportation factor (0 < teleportation factor < 1): "))
    
    # Run PageRank algorithm
    calculate_pagerank(adjacency_matrix, num_iterations, teleportation_factor)

if __name__ == "__main__":
    main()
