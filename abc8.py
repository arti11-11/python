import numpy as np  

# Define a 12-element input array
input_data = np.array([15, 3, 21, 9, 33, 27, 5, 18, 12, 7, 24, 30])  

# Print the input array
print("Input Array:\n", input_data)  

# Sort the array
sorted_input_data = np.sort(input_data)

# Number of elements in each bin
bin_length = 4
total_bins = len(sorted_input_data) // bin_length

# Create bins for mean, boundaries, and median
mean_bin = np.zeros((total_bins, bin_length))  # Bin mean
boundary_bin = np.zeros((total_bins, bin_length))  # Bin boundaries
median_bin = np.zeros((total_bins, bin_length))  # Bin median

# Print initial bins (subarrays)
print("\nInitial Bins (Subarrays):")
for i in range(0, len(sorted_input_data), bin_length):
    bin_data = sorted_input_data[i:i + bin_length]
    print(f"Bin {i // bin_length + 1}: {bin_data}")

# Bin mean
for i in range(0, len(sorted_input_data), bin_length):
    k = i // bin_length    
    mean_value = np.mean(sorted_input_data[i:i + bin_length])
    mean_bin[k, :] = mean_value
print("\nMean Bin:\n", mean_bin)

# Bin boundaries
for i in range(0, len(sorted_input_data), bin_length):
    k = i // bin_length
    min_val = sorted_input_data[i]
    max_val = sorted_input_data[i + bin_length - 1]
    boundary_bin[k, :] = [min_val] * (bin_length // 2) + [max_val] * (bin_length - bin_length // 2)
print("\nBoundary Bin:\n", boundary_bin)

# Bin median
for i in range(0, len(sorted_input_data), bin_length):
    k = i // bin_length
    median_value = np.median(sorted_input_data[i:i + bin_length])
    median_bin[k, :] = median_value
print("\nMedian Bin:\n", median_bin)
