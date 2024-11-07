import pandas as pd 
from collections import defaultdict 
import math 
# Load the dataset 
file_path = "C:\\artik\\data.csv"  
df = pd.read_csv(file_path) 
# Display the database 
print("Database:") 
print(df.to_string(index=False)) 
# Print the number of rows and columns 
print("\nNumber of Rows and Columns in the Dataset:") 
print(df.shape) 
# Calculate and print the individual class probabilities (P(Stolen?)) 
class_counts = df['Stolen?'].value_counts() 
total_rows = len(df) 
print("\nClass Probabilities (P(Stolen?)):") 
for label, count in class_counts.items(): 
print(f"P({label}) = {count}/{total_rows} = {count/total_rows:.2f}") 
# Calculate and print the probability of individual values of attributes 
print("\nProbability of Individual Values of Attributes:") 
for column in df.columns[1:-1]: 
    value_counts = df[column].value_counts() 
    print(f"\nP({column}):") 
    for value, count in value_counts.items(): 
        print(f"P({column}={value}) = {count}/{total_rows} = 
{count/total_rows:.2f}") 
 
# Calculate and print conditional probabilities (P(X|Y)) 
print("\nConditional Probabilities (P(X|Stolen?)):") 
for column in df.columns[1:-1]: 
    for value in df[column].unique(): 
        for stolen_status in df['Stolen?'].unique(): 
            count = len(df[(df[column] == value) & (df['Stolen?'] == stolen_status)]) 
            total = class_counts[stolen_status] 
            print(f"P({column}={value}|Stolen?={stolen_status}) = {count}/{total} = 
{count/total:.2f}") 
 
# Define the new tuple for classification 
new_tuple = {"Color": "Red", "Type": "SUV", "Origin": "Domestic"} 
# Implement Naive Bayes Classification 
def classify_naive_bayes(df, new_tuple): 
    class_probs = {} 
     
    # For storing the probability for yes and no classes 
    yes_prob = 1.0 
    no_prob = 1.0 
     
    for stolen_status in df['Stolen?'].unique(): 
        # Calculate P(Stolen?=stolen_status) 
        prior_prob = class_counts[stolen_status] / total_rows 
        conditional_prob = prior_prob 
 
        # Calculate P(X|Stolen?=stolen_status) for each attribute 
        for column, value in new_tuple.items(): 
            count = len(df[(df[column] == value) & (df['Stolen?'] == stolen_status)]) 
            conditional_prob *= count / class_counts[stolen_status] 
         
        class_probs[stolen_status] = conditional_prob 
         
        # Save the probability for Yes and No classes 
        if stolen_status == "Yes": 
            yes_prob = conditional_prob 
        elif stolen_status == "No": 
            no_prob = conditional_prob 
 
    # Return the class with the highest posterior probability 
    return class_probs, yes_prob, no_prob 
 
# Print the new tuple 
print("\nNew Tuple for Classification:") 
print(new_tuple) 
# Classify the new tuple 
class_probs, yes_prob, no_prob = classify_naive_bayes(df, new_tuple) 
# Print the probabilities of Yes and No classes as P(Stolen?=Yes|X) and 
P(Stolen?=No|X) 
print(f"\nP(Stolen?=Yes|X) = {yes_prob:.5f}") 
print(f"P(Stolen?=No|X) = {no_prob:.5f}") 
# Determine the class with the highest probability 
classified_class = max(class_probs, key=class_probs.get) 
print("\nClassified as:") 
print(classified_class) 
