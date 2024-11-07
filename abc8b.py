import matplotlib.pyplot as plt

# Function to plot bar chart
def plot_bar_chart(data):
    # Creating labels for the data
    labels = [f"Element {i+1}" for i in range(len(data))]
    
    # Plotting the bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(labels, data, color='blue')
    plt.xlabel('Chocolates')
    plt.ylabel('Values')
    plt.title('Bar Chart of User Input Data')
    plt.show()

# Function to plot histogram
def plot_histogram(data):
    # Plotting the histogram
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=5, color='green', edgecolor='black')
    plt.xlabel('Value Range')
    plt.ylabel('Frequency')
    plt.title('Histogram of User Input Data')
    plt.show()

def main():
    # Taking input from the user
    data = list(map(int, input("Enter the dataset (space-separated): ").split()))
    
    # Visualizing the data
    print("\nCreating Bar Chart...")
    plot_bar_chart(data)
    
    print("\nCreating Histogram...")
    plot_histogram(data)

if __name__ == "__main__":
    main()
