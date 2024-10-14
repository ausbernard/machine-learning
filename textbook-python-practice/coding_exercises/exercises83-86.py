## https://www.freecodecamp.org/news/python-set-operations-explained-with-examples/

# Exercise 83
# Write a function definition named get_unique_values that takes in a list and returns a set with only the unique values from that list.

def get_unique_values(sequence):
    # This property of sets is useful in many situations where you want to avoid repetition in your data.
    return set(sequence)

assert get_unique_values(["ant", "ant", "mosquito", "mosquito", "ladybug"]) == {"ant", "mosquito", "ladybug"}
assert get_unique_values(["b", "a", "n", "a", "n", "a", "s"]) == {"b", "a", "n", "s"}
assert get_unique_values(["mary", "had", "a", "little", "lamb", "little", "lamb", "little", "lamb"]) == {"mary", "had", "a", "little", "lamb"}
print("Exercise 83 is correct.")

# Exercise 84
# Write a function definition named get_unique_values_from_two_lists that takes two lists and returns a single set with only the unique values

def get_unique_values_from_two_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.union(set2)

assert get_unique_values_from_two_lists([5, 1, 2, 3], [3, 4, 5, 5]) == {1, 2, 3, 4, 5}
assert get_unique_values_from_two_lists([1, 1], [2, 2, 3]) == {1, 2, 3}
assert get_unique_values_from_two_lists(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"tomato", "mango", "kiwi", "eggplant", "broccoli"}
print("Exercise 84 is correct.")

# Exercise 85
# Write a function definition named get_values_in_common that takes two lists and returns a single set with the values that each list has in common

def get_values_in_common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

assert get_values_in_common([5, 1, 2, 3], [3, 4, 5, 5]) == {3, 5}
assert get_values_in_common([1, 2], [2, 2, 3]) == {2}
assert get_values_in_common(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"tomato"}
print("Exercise 85 is correct.")

# Exercise 86
# Write a function definition named get_values_not_in_common that takes two lists and returns a single set with the values that each list does not have in common
def get_values_not_in_common(list1, list2):
    set1 = set(list1) 
    set2 = set(list2)
    # set1diff = set1 - set2
    # set2diff = set2 - set1
    # return set1diff.union(set2diff)
    return set1.symmetric_difference(set2)


assert get_values_not_in_common([5, 1, 2, 3], [3, 4, 5, 5]) == {1, 2, 4}
assert get_values_not_in_common([1, 1], [2, 2, 3]) == {1, 2, 3}
assert get_values_not_in_common(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"mango", "kiwi", "eggplant", "broccoli"}
print("Exercise 86 is correct.")