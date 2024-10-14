import math

def probability_of_height_k(k,p):
    return (p**k) * (1 - p)

def worst_case(n,p):
    if p <= 0 or p >= 1:
        raise ValueError("p must be in the range (0, 1)")
    
    return 1 + (1 / p) * (math.log(n) / math.log(p)) + (1 / (1 - p))

k = 2
p = 0.025
n = 1000000
probability = probability_of_height_k(k, p)
print(f"The probability that a new node will have a height of {k} is {probability:.4f}")

worst_case_result = worst_case(n, p)
print(f"The worst case for n={n} and p={p} is {worst_case_result:.4f}")

"""
    Interpretation of the Value: If you're using a logarithmic function and the result is negative, it may indicate that 
𝑛
n (the size of the skip list) is less than 
𝑝
p (the probability factor). In practical terms, this could mean that the structure of the skip list is not optimal given the parameters you provided.

Theoretical Context: In a well-structured skip list, you expect positive values, representing the average or expected number of comparisons to find an element. A negative result could suggest that the configuration (like p or n) isn't appropriate for your dataset or that you're looking at a scenario where the list is effectively empty or poorly balanced.

The expected height (ℎ) of the skip list is logarithmic in relation to the number of elements (n)
h≈log1/p(n)
for instance log2(n) would be a p of 0.5

At ( p = 0.5: This is a balanced choice, providing a good trade-off between speed and memory usage.
At ( p = 0.8: Searches can be faster, but memory usage increases and it may become unbalanced.
At ( p = 0.2: Searches may take longer, but the structure is more memory-efficient and better balanced.

Stick with 𝑝=0.5 for a good balance.
If your application requires fast searches and can tolerate higher memory usage, consider a higher 𝑝.

If memory efficiency is critical and your dataset can accommodate longer search times, a lower 𝑝 could be beneficial.
"""