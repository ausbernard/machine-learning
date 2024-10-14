# notes
"""
# Binary search is done on a sorted list or a sorted array. 
# Binary search takes the length of the list (minus one) and divides it by two -- this becomes the check index. 
# If the value at the check index is less than our 'search for input' then that number becomes the new start of our index. 
# If the value at the check index value is more than our 'search for input' then that index becomes our end and the beginning is still the start index. 
# We use recursion until the number is either found or isn't found. 
# || https://www.cs.usfca.edu/~galles/visualization/Search.html
"""
# generate array
"""
# import random
# import array

# sample_list = random.sample(range(1, 101), 15)
# sample_array = array.array("i", sample_list)

# sorted_sample_array = sorted(sample_array)

# print("Sample Array:", sample_array)
# print("Sorted Sample Array:", sorted_sample_array)
"""

def binary_search(array, search_element):
    # initialize "left" and "right" indices
    left = 0
    right = len(array) - 1
    
    # start a while loop that loops indefinitely until the condition is False
    while left <= right:
        # compute the middle index
        middle = (right + left) // 2
        # if the search element equals the middle element we found it
        if search_element == array[middle]:
            return True
        # if the search element is larger than the middle element  "recurse" right
        if search_element > array[middle]:
            left = middle + 1
        # if the search element is smaller than the middle element "recurse" left
        if search_element < array[middle]:
            right = middle - 1
    return -1
    # return False

# return -1 then it is false
print(binary_search([11, 13, 18, 24, 35, 38, 40, 49, 51, 59, 65, 77, 79, 81, 97], 35))

#algorithmic time complexity
"""
# The number of iterations required to reduce the search space to 1 element is logarithmic with respect to the number of elements in an array. At most it would take O(log(n)) iterations where n is the number of elements in an array

# mathematically we are halving our search space size each time

1. search space (n)
2. search space is (n/2)
3. search space is (n/4)
...
∞. after k iterations, the search space is (n/2**k) (n/2^k)
mathematically: n / 2^k = 1
so [ \log_2(n) = k ]
therefore drop the constant O(log(n))
"""