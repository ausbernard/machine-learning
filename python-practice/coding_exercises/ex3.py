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

