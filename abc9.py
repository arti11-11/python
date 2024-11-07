from itertools import combinations 
from collections import defaultdict 
 
def get_frequent_itemsets(transactions, min_support): 
    item_count = defaultdict(int) 
    
    # Count each item in the transactions 
    for transaction in transactions: 
        for item in transaction: 
            item_count[item] += 1 
 
    # Candidate sets for iteration 0 (single items) 
    candidate_sets = {frozenset([item]): count for item, count in item_count.items()} 
    
    # Print candidate sets for iteration 0 
    print(f"Iteration 0: Candidate sets and their support values:") 
    for itemset, count in candidate_sets.items(): 
        print(f"Candidate: {set(itemset)}, Support: {count}") 
    
    # Filter items based on minimum support 
    frequent_itemsets = {itemset: count for itemset, count in candidate_sets.items() if count >= 
min_support} 
    all_frequent_itemsets = dict(frequent_itemsets) 
    
    # Print frequent itemsets for iteration 0 
    print(f"Iteration 0: Frequent itemsets (after filtering):") 
    for itemset, count in frequent_itemsets.items(): 
        print(f"Frequent Itemset: {set(itemset)}, Support: {count}") 
 
    k = 2  # Start with 2-itemsets 
    while frequent_itemsets: 
        candidate_sets = defaultdict(int) 
        
        # Generate candidates of size k 
        itemsets = list(frequent_itemsets.keys()) 
        for i, itemset1 in enumerate(itemsets): 
            for itemset2 in itemsets[i+1:]: 
                union_set = itemset1.union(itemset2) 
                if len(union_set) == k: 
                    candidate_sets[union_set] = 0 
        
        # Count support for candidate sets 
 
        for transaction in transactions: 
            transaction_set = frozenset(transaction) 
            for candidate in candidate_sets: 
                if candidate.issubset(transaction_set): 
                    candidate_sets[candidate] += 1 
        
        # Print all candidate sets and their support values (before filtering) 
        print(f"Iteration {k-1}: Candidate sets and their support values:") 
        for itemset, count in candidate_sets.items(): 
            print(f"Candidate: {set(itemset)}, Support: {count}") 
        
        # Filter candidates based on minimum support 
        frequent_itemsets = {itemset: count for itemset, count in candidate_sets.items() if count >= 
min_support} 
        all_frequent_itemsets.update(frequent_itemsets) 
        
        # Print frequent itemsets for this iteration 
        print(f"Iteration {k-1}: Frequent itemsets (after filtering):") 
        for itemset, count in frequent_itemsets.items(): 
            print(f"Frequent Itemset: {set(itemset)}, Support: {count}") 
        
        if not frequent_itemsets: 
            print(f"Iteration {k-1}: No more frequent itemsets found.") 
            break 
        
        k += 1 
    
    return all_frequent_itemsets 
 
def print_association_rules(frequent_itemsets, min_confidence): 
    rules = [] 
    
    for itemset in frequent_itemsets: 
        # Only consider itemsets with more than 1 item for association rules 
        if len(itemset) > 1: 
            for i in range(1, len(itemset)): 
                for subset in combinations(itemset, i): 
                    subset = frozenset(subset) 
                    remainder = itemset.difference(subset) 
                    # Allow rules with one item on one side, but prevent single-item-to-single-item 
                    if len(subset) > 0 and len(remainder) > 0 and not (len(subset) == 1 and 
len(remainder) == 1): 
                        if subset in frequent_itemsets: 
                            confidence = frequent_itemsets[itemset] / frequent_itemsets[subset] 

                            if confidence >= min_confidence: 
                                rules.append((subset, remainder, confidence)) 
    
    return rules 
 
# Sample Transactions 
transactions = [ 
    ['1', '3', '4'], 
    ['2', '3','5'], 
    ['1', '2','3','5'], 
    ['2', '5'], 
] 
 
# Compute minimum support based on 50% of the number of transactions 
min_support = int(0.50 * len(transactions))  # 50% of 4 transactions = 2 
min_confidence = 0.50  # 50% 
 
# Step 1: Print number of transactions 
print(f"Number of transactions: {len(transactions)}") 
 
# Step 2: Print number of items in transactions 
num_items = sum(len(transaction) for transaction in transactions) 
print(f"Number of items in transactions: {num_items}") 
 
# Step 3: Find frequent itemsets 
frequent_itemsets = get_frequent_itemsets(transactions, min_support) 
 
# Final Frequent Item Set 
print(f"Final Frequent Item Set: {list(frequent_itemsets.keys())}") 
 
# Step 4: Print association rules 
association_rules = print_association_rules(frequent_itemsets, min_confidence) 
print("Association Rules:") 
for rule in association_rules: 
    antecedent, consequent, confidence = rule 
    print(f"{set(antecedent)} -> {set(consequent)}, confidence: {confidence:.2f}")
