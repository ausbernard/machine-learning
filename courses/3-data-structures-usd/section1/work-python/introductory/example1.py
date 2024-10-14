import random

# list of n numbers
numbers = [random.randint(1, 100) for _ in range(10)]
# for each number in the list, we want to print out the number and it's opposite
for number in numbers:
    print("Operation 1:Print Itself")
    print(number)
    print("Operation 2: Return the opposite")
    opposite = (number * -1)
    print("Operation 3: Print the opposite")
    print(opposite)
    print("======================")
    
# No matter how many elements or numbers our algorithm will perform exactly 3(n) because there exists some constant (which is 3) for which the number of operations performed by the algorithm is always bounded by the function g(n) = n
