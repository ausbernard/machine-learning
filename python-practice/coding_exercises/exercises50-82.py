import statistics
import math


# Exercise 50
# Write a function definition named first that takes in sequence and returns the first value of that sequence.

def first(sequence):
    return sequence[0]

assert first("ubuntu") == "u"
assert first([1, 2, 3]) == 1
assert first(["python", "is", "awesome"]) == "python"
print("Exercise 50 is correct.")

# Exercise 51
# Write a function definition named second that takes in sequence and returns the second value of that sequence.

def second(sequence):
    return sequence[1]

assert second("ubuntu") == "b"
assert second([1, 2, 3]) == 2
assert second(["python", "is", "awesome"]) == "is"
print("Exercise 51 is correct.")

# Exercise 52
# Write a function definition named third that takes in sequence and returns the third value of that sequence.
def third(sequence):
    return sequence[2]

assert third("ubuntu") == "u"
assert third([1, 2, 3]) == 3
assert third(["python", "is", "awesome"]) == "awesome"
print("Exercise 52 is correct.")

# Exercise 53
# Write a function definition named forth that takes in sequence and returns the forth value of that sequence.
def forth(sequence):
    return sequence[3]

assert forth("ubuntu") == "n"
assert forth([1, 2, 3, 4]) == 4
assert forth(["python", "is", "awesome", "right?"]) == "right?"
print("Exercise 53 is correct.")

# Exercise 54
# Write a function definition named last that takes in sequence and returns the last value of that sequence.
def last(sequence):
    return sequence[-1]

assert last("ubuntu") == "u"
assert last([1, 2, 3, 4]) == 4
assert last(["python", "is", "awesome"]) == "awesome"
assert last(["kiwi", "mango", "guava"]) == "guava"
print("Exercise 54 is correct.")

# Exercise 55
# Write a function definition named second_to_last that takes in sequence and returns the second to last value of that sequence.
def second_to_last(sequence):
    return sequence[-2]

assert second_to_last("ubuntu") == "t"
assert second_to_last([1, 2, 3, 4]) == 3
assert second_to_last(["python", "is", "awesome"]) == "is"
assert second_to_last(["kiwi", "mango", "guava"]) == "mango"
print("Exercise 55 is correct.")

# Exercise 56
# Write a function definition named third_to_last that takes in sequence and returns the third to last value of that sequence.
def third_to_last(sequence):
    return sequence[-3]

assert third_to_last("ubuntu") == "n"
assert third_to_last([1, 2, 3, 4]) == 2
assert third_to_last(["python", "is", "awesome"]) == "python"
assert third_to_last(["strawberry", "kiwi", "mango", "guava"]) == "kiwi"
print("Exercise 56 is correct.")

# Exercise 57
# Write a function definition named first_and_second that takes in sequence and returns the first and second value of that sequence as a list
def first_and_second(sequence):
    return sequence[0:2]

assert first_and_second([1, 2, 3, 4]) == [1, 2]
assert first_and_second(["python", "is", "awesome"]) == ["python", "is"]
assert first_and_second(["strawberry", "kiwi", "mango", "guava"]) == ["strawberry", "kiwi"]
print("Exercise 57 is correct.")

# Exercise 58
# Write a function definition named first_and_last that takes in sequence and returns the first and last value of that sequence as a list
def first_and_last(sequence):
    return [sequence[0], sequence[-1]]

assert first_and_last([1, 2, 3, 4]) == [1, 4]
assert first_and_last(["python", "is", "awesome"]) == ["python", "awesome"]
assert first_and_last(["strawberry", "kiwi", "mango", "guava"]) == ["strawberry", "guava"]
print("Exercise 58 is correct.")

# Exercise 59
# Write a function definition named first_to_last that takes in sequence and returns the sequence with the first value moved to the end of the sequence.
def first_to_last(sequence):
    element = sequence.pop(0)
    sequence.append(element)
    return sequence

assert first_to_last([1, 2, 3, 4]) == [2, 3, 4, 1]
assert first_to_last(["python", "is", "awesome"]) == ["is", "awesome", "python"]
assert first_to_last(["strawberry", "kiwi", "mango", "guava"]) == ["kiwi", "mango", "guava", "strawberry"]
print("Exercise 59 is correct.")

# Exercise 60
# Write a function definition named sum_all that takes in sequence of numbers and returns all the numbers added together.

def sum_all(sequence):
    #Time for the 'sum' method: 6.668483738
    #Time for the 'for loop' method: 41.574598955
    return sum(sequence)
    # return sum(number for number in sequence)

assert sum_all([1, 2, 3, 4]) == 10
assert sum_all([3, 3, 3]) == 9
assert sum_all([0, 5, 6]) == 11
print("Exercise 60 is correct.")

# Exercise 61
# Write a function definition named mean that takes in sequence of numbers and returns the average value
def mean(sequence):
    # In general, if you're working with a large sequence and you're concerned about memory usage, you might want to use a generator expression. But if speed is more important and you're not concerned about memory usage, using a list can be faster.
    # list
    return sum(sequence) / len(sequence)
    # generator expression
    # return sum(number for number in sequence) / len(sequence)

assert mean([1, 2, 3, 4]) == 2.5
assert mean([3, 3, 3]) == 3
assert mean([1, 5, 6]) == 4
print("Exercise 61 is correct.")

# Exercise 62
# Write a function definition named median that takes in sequence of numbers and returns the average value
def median(sequence):
    # for median data needs to be sorted in order from least to greatest
    sequence = sorted(sequence)
    data_length = len(sequence)
    middle_element = (data_length//2)
    # median can be calculated with the length of the sequence (odd or even) by calculating the middle
    # if length is divisible by 2 middle is (even)
    if data_length % 2 == 0:
        # take the element to the left and right of the middle and divide it by 2
        right_element = sequence[middle_element]
        left_element = sequence[middle_element - 1]
        # calculate the average
        return (left_element + right_element) / 2
    else:
        # find the middle element position
        middle_element = sequence[middle_element]
        return middle_element / 1     
    
assert median([1, 5, 3, 4, 2]) == 3.0
assert median([1, 2, 3]) == 2.0
assert median([1, 5, 6]) == 5.0
assert median([1, 2, 5, 6]) == 3.5
print("Exercise 62 is correct.")

# Exercise 63
# Write a function definition named mode that takes in sequence of numbers and returns the most commonly occurring value

def mode(sequence):
    dict_tracker = {}
    for number in sequence:
        if number not in dict_tracker:
            dict_tracker[number] = 1
        else:
            dict_tracker[number] += 1
    
    return max(dict_tracker, key=dict_tracker.get)

def key_with_max_value(dict_tracker):
    max_value = None
    max_key = None
    for key, value in dict_tracker.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key
    return max_key
        
assert mode([1, 2, 2, 3, 4]) == 2
assert mode([1, 1, 2, 3]) == 1
assert mode([2, 2, 3, 3, 3]) == 3
print("Exercise 63 is correct.")

# Exercise 64
# Write a function definition named product_of_all that takes in sequence of numbers and returns the product of multiplying all the numbers together

def product_of_all(sequence):
    # n = 200
    # Time for your 'product_of_all' function: 5.380983012
    # Time for the 'math.prod' function: 1.1387402819999997
    return math.prod(sequence)
    # product_total = 1
    # for number in sequence:
    #     product_total *= number
    # return product_total

assert product_of_all([1, 2, 3]) == 6
assert product_of_all([3, 4, 5]) == 60
assert product_of_all([2, 2, 3, 0]) == 0
print("Exercise 64 is correct.")

# Exercise 65
# Write a function definition named get_highest_number that takes in sequence of numbers and returns the largest number.

def get_highest_number(sequence):
    # n = 2000
    # Time for your 'get_highest_number' function: 95.838375709
    # Time for the 'max()' function: 14.062962800999998
    return max(sequence)
    # dict_tracker = {}
    # for number in sequence:
    #     dict_tracker[number] = 0
    # return max(dict_tracker)
    
assert get_highest_number([1, 2, 3]) == 3
assert get_highest_number([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 5
assert get_highest_number([-5, -3, 1]) == 1
print("Exercise 65 is correct.")

# Exercise 66
# Write a function definition named get_smallest_number that takes in sequence of numbers and returns the smallest number.

def get_smallest_number(sequence):
    # n = 2000
    # Time for your 'get_highest_number' function: 95.838375709
    # Time for the 'max()' function: 14.062962800999998
    return min(sequence)
    # dict_tracker = {}
    # for number in sequence:
    #     dict_tracker[number] = 0
    # return min(dict_tracker)

assert get_smallest_number([1, 3, 2]) == 1
assert get_smallest_number([5, -5, -4, -3, -2, -1, 1, 2, 3, 4]) == -5
assert get_smallest_number([-4, -3, 1, -10]) == -10
print("Exercise 66 is correct.")

# Exercise 67
# Write a function definition named only_odd_numbers that takes in sequence of numbers and returns the odd numbers in a list.
def only_odd_numbers(sequence):
    # small sequence sizes
    # n =  50
    # Time for your 'only_odd_numbers' function: 6.485567668
    # Time for the list comprehension: 4.511601152
    odds = []
    for number in sequence:
        if number % 2 != 0:
            odds.append(number)
    return odds
    # large sequence sizes
    # n = 2000
    # Time for your 'only_odd_numbers' function: 62.191144969
    # Time for the list comprehension: 45.316702963
    # return [number for number in sequence if number %2 != 0]

assert only_odd_numbers([1, 2, 3]) == [1, 3]
assert only_odd_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -3, -1, 1, 3, 5]
assert only_odd_numbers([-4, -3, 1]) == [-3, 1]
assert only_odd_numbers([2, 2, 2, 2, 2]) == []
print("Exercise 67 is correct.")

# Exercise 68
# Write a function definition named only_even_numbers that takes in sequence of numbers and returns the even numbers in a list.

def only_even_numbers(sequence):
    evens = []
    for number in sequence:
        if number % 2 == 0:
            evens.append(number)
    return evens
    # large sequence sizes
    # n = 2000
    # Time for your 'only_even_numbers' function: 62.191144969
    # Time for the list comprehension: 45.316702963
    # return [number for number in sequence if number %2 == 0]

assert only_even_numbers([1, 2, 3]) == [2]
assert only_even_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-4, -2, 2, 4]
assert only_even_numbers([-4, -3, 1]) == [-4]
assert only_even_numbers([1, 1, 1, 1, 1, 1]) == []
print("Exercise 68 is correct.")

# Exercise 69
# Write a function definition named only_positive_numbers that takes in sequence of numbers and returns the positive numbers in a list.
def only_positive_numbers(sequence):
    return [number for number in sequence if number > 0]

assert only_positive_numbers([1, 2, 3]) == [1, 2, 3]
assert only_positive_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert only_positive_numbers([-4, -3, 1]) == [1]
print("Exercise 69 is correct.")

# Exercise 70
# Write a function definition named only_negative_numbers that takes in sequence of numbers and returns the negative numbers in a list.
def only_negative_numbers(sequence):
    return [number for number in sequence if number < 0]

assert only_negative_numbers([1, 2, 3]) == []
assert only_negative_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -4, -3, -2, -1]
assert only_negative_numbers([-4, -3, 1]) == [-4, -3]
print("Exercise 70 is correct.")

# Exercise 71
# Write a function definition named has_evens that takes in sequence of numbers and returns True if there are any even numbers in the sequence

def has_evens(sequence):
    return any(number % 2 == 0 for number in sequence)

assert has_evens([1, 2, 3]) == True
assert has_evens([2, 5, 6]) == True
assert has_evens([3, 3, 3]) == False
assert has_evens([]) == False
print("Exercise 71 is correct.")

# Exercise 72
# Write a function definition named count_evens that takes in sequence of numbers and returns the number of even numbers
def count_evens(sequence):
    # count = 0
    # for number in sequence:
    #     if number % 2 == 0:
    #         count += 1
    # return count
    return len([number for number in sequence if number % 2 == 0])
    
assert count_evens([1, 2, 3]) == 1
assert count_evens([2, 5, 6]) == 2
assert count_evens([3, 3, 3]) == 0
assert count_evens([5, 6, 7, 8] ) == 2
print("Exercise 72 is correct.")

# Exercise 73
# Write a function definition named has_odds that takes in sequence of numbers and returns True if there are any odd numbers in the sequence
def has_odds(sequence):
    return any(number % 2 != 0 for number in sequence)

assert has_odds([1, 2, 3]) == True
assert has_odds([2, 5, 6]) == True
assert has_odds([3, 3, 3]) == True
assert has_odds([2, 4, 6]) == False
print("Exercise 73 is correct.")

# Exercise 74
# Write a function definition named count_odds that takes in sequence of numbers and returns True if there are any odd numbers in the sequence
def count_odds(sequence):
    return len([number for number in sequence if number % 2 != 0])

assert count_odds([1, 2, 3]) == 2
assert count_odds([2, 5, 6]) == 1
assert count_odds([3, 3, 3]) == 3
assert count_odds([2, 4, 6]) == 0
print("Exercise 74 is correct.")

# Exercise 75
# Write a function definition named count_negatives that takes in sequence of numbers and returns a count of the number of negative numbers

def count_negatives(sequence):
    return len([number for number in sequence if number < 0])

assert count_negatives([1, -2, 3]) == 1
assert count_negatives([2, -5, -6]) == 2
assert count_negatives([3, 3, 3]) == 0
print("Exercise 75 is correct.")

# Exercise 76
# Write a function definition named count_positives that takes in sequence of numbers and returns a count of the number of positive numbers

def count_positives(sequence):
    return len([number for number in sequence if number > 0])

assert count_positives([1, -2, 3]) == 2
assert count_positives([2, -5, -6]) == 1
assert count_positives([3, 3, 3]) == 3
assert count_positives([-2, -1, -5]) == 0
print("Exercise 76 is correct.")

# Exercise 77
# Write a function definition named only_positive_evens that takes in sequence of numbers and returns a list containing all the positive evens from the sequence
def only_positive_evens(sequence):
    return [number for number in sequence if number > 0 and number % 2 == 0]

assert only_positive_evens([1, -2, 3]) == []
assert only_positive_evens([2, -5, -6]) == [2]
assert only_positive_evens([3, 3, 4, 6]) == [4, 6]
assert only_positive_evens([2, 3, 4, -1, -5]) == [2, 4]
print("Exercise 77 is correct.")

# Exercise 78
# Write a function definition named only_positive_odds that takes in sequence of numbers and returns a list containing all the positive odd numbers from the sequence
def only_positive_odds(sequence):
    return [number for number in sequence if number > 0 and number % 2 != 0]

assert only_positive_odds([1, -2, 3]) == [1, 3]
assert only_positive_odds([2, -5, -6]) == []
assert only_positive_odds([3, 3, 4, 6]) == [3, 3]
assert only_positive_odds([2, 3, 4, -1, -5]) == [3]
print("Exercise 78 is correct.")

# Exercise 79
# Write a function definition named only_negative_evens that takes in sequence of numbers and returns a list containing all the negative even numbers from the sequence
def only_negative_evens(sequence):
    return [number for number in sequence if number < 0 and number % 2 == 0]

assert only_negative_evens([1, -2, 3]) == [-2]
assert only_negative_evens([2, -5, -6]) == [-6]
assert only_negative_evens([3, 3, 4, 6]) == []
assert only_negative_evens([-2, 3, 4, -1, -4]) == [-2, -4]
print("Exercise 79 is correct.")

# Exercise 80
# Write a function definition named only_negative_odds that takes in sequence of numbers and returns a list containing all the negative odd numbers from the sequence
def only_negative_odds(sequence):
    return [number for number in sequence if number < 0 and number % 2 != 0]

assert only_negative_odds([1, -2, 3]) == []
assert only_negative_odds([2, -5, -6]) == [-5]
assert only_negative_odds([3, 3, 4, 6]) == []
assert only_negative_odds([2, -3, 4, -1, -4]) == [-3, -1]
print("Exercise 80 is correct.")