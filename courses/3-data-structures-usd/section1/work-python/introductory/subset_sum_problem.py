#subset sum problem  -- verifies doesn't solve

def check_subset(set, subset):
    # verify that the subset is a valid non-empty subset of set
    if not subset:
        return False        # O(1)
    for element in subset:      #O(n)
        if element not in set:
            return False
    
    # verify that the elements of the subset add up to 0
    sum = 0     #  O(n)
    for element in subset:
        sum = sum + element
    if sum == 0:        # O(1)
        return True
    else:
        return False
# Verifies in polynomial O(2n+2) ->-> O(n) time.

    
# Sample dataset: Test cases give you a set of integers set and a proposed answer subset, you would be able to check the correctness of subset in polynomial time:
set = {1, -1, 2, -2, 3, -3, 4, -4}

subsets = [
    {1, -1},        # Valid subset, sums to 0
    {2, -2, 3, -3}, # Valid subset, sums to 0
    {4, -4},        # Valid subset, sums to 0
    {1, 2, 3},      # Invalid subset, does not sum to 0
    {},             # Invalid subset, empty
    {5, -5},        # Invalid subset, elements not in set
]

for subset in subsets:
    result = check_subset(set, subset)
    print(f"Subset: {subset}, Result: {result}")