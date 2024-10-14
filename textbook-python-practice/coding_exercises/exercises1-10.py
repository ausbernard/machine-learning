# Exercise 1
# On the line below, create a variable named on_mars_right_now and assign it the boolean value of False

on_mars_right_now = False

assert on_mars_right_now == False, "If you see a Name Error, be sure to create the variable and assign it a value."
print("Exercise 1 is correct.")

# Exercise 2
# Create a variable named fruits and assign it a list of fruits containing the following fruit names as strings: 
# mango, banana, guava, kiwi, and strawberry.

fruits = ["mango", "banana", "guava", "kiwi", "strawberry"]

assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry"], "If you see an Assert Error, ensure the variable contains all the strings in the provided order"
print("Exercise 2 is correct.")

# Exercise 3
# Create a variable named vegetables and assign it a list of fruits containing the following vegetable names as strings: 
# eggplant, broccoli, carrot, cauliflower, and zucchini

veg_string="eggplant, broccoli, carrot, cauliflower, and zucchini"
# Strip 'and'
vegetables = veg_string.replace('and','').replace('  ', ' ')
# Convert veg_string into a comma separated list of strings
vegetables = vegetables.split(", ")

assert vegetables == ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini"], "Ensure the variable contains all the strings in the provided order"
print("Exercise 3 is correct.")

# Exercise 4
# Create a variable named numbers and assign it a list of numbers, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Ensure the variable contains the numbers 1-10 in order."
print("Exercise 4 is correct.")

# Exercise 5
# Given the following assignment of the list of fruits, add "tomato" to the end of the list. 

fruits = ["mango", "banana", "guava", "kiwi", "strawberry"]

fruits.append("tomato")

assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"], "Ensure the variable contains all the strings in the right order"
print("Exercise 5 is correct.")

# Exercise 6
# Given the following assignment of the vegetables list, add "tomato" to the end of the list.
vegetables = ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini"]

vegetables.append("tomato")

assert vegetables == ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini", "tomato"], "Ensure the variable contains all the strings in the provided order"
print("Exercise 6 is correct.")

# Exercise 7
# Given the list of numbers defined below, reverse the list of numbers that you created above. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#reverse list in place
numbers.reverse()

assert numbers == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "Assert Error means that the answer is incorrect." 
print("Exercise 7 is correct.")

# Exercise 8
# Sort the vegetables in alphabetical order

vegetables = ["eggplant", "tomato", "broccoli", "carrot", "cauliflower", "zucchini"]

vegetables.sort()

assert vegetables == ['broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
print("Exercise 8 is correct.") 

# Exercise 9
# Write the code necessary to sort the fruits in reverse alphabetical order

fruits = ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"]

fruits.sort(reverse=True)

assert fruits == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana']
print("Exercise 9 is correct.")

# Exercise 10
# Write the code necessary to produce a single list that holds all fruits then all vegetables in the order as they were sorted above.

fruits = ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"]
vegetables = ["eggplant", "tomato", "broccoli", "carrot", "cauliflower", "zucchini"]
fruits.sort(reverse=True)
vegetables.sort()
fruits_and_veggies = fruits + vegetables

assert fruits_and_veggies == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana', 'broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
print("Exercise 10 is correct.")