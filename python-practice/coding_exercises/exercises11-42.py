# Run this cell in order to generate some numbers to use in our functions after this.
import random
import math

fruits = ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"]
vegetables = ["eggplant", "tomato", "broccoli", "carrot", "cauliflower", "zucchini"]
    
positive_even_number = random.randrange(2, 101, 2)
negative_even_number = random.randrange(-100, -1, 2)

positive_odd_number = random.randrange(1, 100, 2)
negative_odd_number = random.randrange(-101, 0, 2)
print("We now have some random numbers available for future exercises.")
print("The random positive even number is", positive_even_number)
print("The random positive odd number is", positive_odd_number)
print("The random negative even number", negative_even_number)
print("The random negative odd number", negative_odd_number)

# Exercise 11
# Write a function definition for a function named add_one that takes in a number and returns that number plus one.
def add_one(number):
    return number + 1

assert add_one(2) == 3, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(0) == 1, "Zero plus one is one."
assert add_one(positive_even_number) == positive_even_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(negative_odd_number) == negative_odd_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 11 is correct.") 

# Exercise 12
# Write a function definition named is_positive that takes in a number and returns True or False if that number is positive.

def is_positive(number):
    if number > 0:
        return True
    else:
        return False
    
assert is_positive(positive_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(positive_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(0) == False, "Zero is not a positive number."
print("Exercise 12 is correct.")

# Exercise 13
# Write a function definition named is_negative that takes in a number and returns True or False if that number is negative.

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

assert is_negative(positive_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(positive_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(negative_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(negative_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(0) == False, "Zero is not a negative number."
print("Exercise 13 is correct.")

# Exercise 14
# Write a function definition named is_odd that takes in a number and returns True or False if that number is odd.

def is_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True

assert is_odd(positive_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(positive_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(negative_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(negative_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 14 is correct.")

# Exercise 15
# Write a function definition named is_even that takes in a number and returns True or False if that number is even.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
assert is_even(2) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(positive_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(positive_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(negative_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(negative_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 15 is correct.")

# Exercise 16
# Write a function definition named identity that takes in any argument and returns that argument's value. Don't overthink this one!
def identity(argument):
    return argument

assert identity(fruits) == fruits, "Ensure that the function is defined, named properly, and returns the correct value"
assert identity(vegetables) == vegetables, "Ensure that the function is defined, named properly, and returns the correct value"
assert identity(positive_odd_number) == positive_odd_number, "Ensure that the function is defined, named properly, and returns the correct value"
assert identity(positive_even_number) == positive_even_number, "Ensure that the function is defined, named properly, and returns the correct value"
assert identity(negative_odd_number) == negative_odd_number, "Ensure that the function is defined, named properly, and returns the correct value"
assert identity(negative_even_number) == negative_even_number, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 16 is correct.")

# Exercise 17
# Write a function definition named is_positive_odd that takes in a number and returns True or False if the value is both greater than zero and odd

def is_positive_odd(number):
    if number > 0 and number % 2 != 0:
        return True
    else:
        return False

assert is_positive_odd(3) == True, "Double check your syntax and logic" 
assert is_positive_odd(positive_odd_number) == True, "Double check your syntax and logic"
assert is_positive_odd(positive_even_number) == False, "Double check your syntax and logic"
assert is_positive_odd(negative_odd_number) == False, "Double check your syntax and logic"
assert is_positive_odd(negative_even_number) == False, "Double check your syntax and logic"
print("Exercise 17 is correct.")

# Exercise 18
# Write a function definition named is_positive_even that takes in a number and returns True or False if the value is both greater than zero and even
def is_positive_even(number):
    if number > 0 and number % 2 == 0:
        return True
    else:
        return False

assert is_positive_even(4) == True, "Double check your syntax and logic" 
assert is_positive_even(positive_odd_number) == False, "Double check your syntax and logic"
assert is_positive_even(positive_even_number) == True, "Double check your syntax and logic"
assert is_positive_even(negative_odd_number) == False, "Double check your syntax and logic"
assert is_positive_even(negative_even_number) == False, "Double check your syntax and logic"
print("Exercise 18 is correct.")

# Exercise 19
# Write a function definition named is_negative_odd that takes in a number and returns True or False if the value is both less than zero and odd.

def is_negative_odd(number):
    if number < 0 and number % 2 != 0:
        return True
    else: 
        return False

assert is_negative_odd(-3) == True, "Double check your syntax and logic" 
assert is_negative_odd(positive_odd_number) == False, "Double check your syntax and logic"
assert is_negative_odd(positive_even_number) == False, "Double check your syntax and logic"
assert is_negative_odd(negative_odd_number) == True, "Double check your syntax and logic"
assert is_negative_odd(negative_even_number) == False, "Double check your syntax and logic"
print("Exercise 19 is correct.")

# Exercise 20
# Write a function definition named is_negative_even that takes in a number and returns True or False if the value is both less than zero and even.

def is_negative_even(number):
    if number < 0 and number % 2 == 0:
        return True
    else:
        return False 

assert is_negative_even(-4) == True, "Double check your syntax and logic" 
assert is_negative_even(positive_odd_number) == False, "Double check your syntax and logic"
assert is_negative_even(positive_even_number) == False, "Double check your syntax and logic"
assert is_negative_even(negative_odd_number) == False, "Double check your syntax and logic"
assert is_negative_even(negative_even_number) == True, "Double check your syntax and logic"
print("Exercise 20 is correct.")

# Exercise 21
# Write a function definition named half that takes in a number and returns half the provided number.

def half(number):
    return number / 2

assert half(4) == 2
assert half(5) == 2.5
assert half(positive_odd_number) == positive_odd_number / 2
assert half(positive_even_number) == positive_even_number / 2
assert half(negative_odd_number) == negative_odd_number / 2
assert half(negative_even_number) == negative_even_number / 2
print("Exercise 21 is correct.")

# Exercise 22
# Write a function definition named double that takes in a number and returns double the provided number.

def double(number):
    return number * 2

assert double(4) == 8
assert double(5) == 10
assert double(positive_odd_number) == positive_odd_number * 2
assert double(positive_even_number) == positive_even_number * 2
assert double(negative_odd_number) == negative_odd_number * 2
assert double(negative_even_number) == negative_even_number * 2
print("Exercise 22 is correct.")

# Exercise 23
# Write a function definition named triple that takes in a number and returns triple the provided number.

def triple(number):
    return number * 3

assert triple(4) == 12
assert triple(5) == 15
assert triple(positive_odd_number) == positive_odd_number * 3
assert triple(positive_even_number) == positive_even_number * 3
assert triple(negative_odd_number) == negative_odd_number * 3
assert triple(negative_even_number) == negative_even_number * 3
print("Exercise 23 is correct.")

# Exercise 24
# Write a function definition named reverse_sign that takes in a number and returns the provided number but with the sign reversed.

def reverse_sign(number):
    return -number

assert reverse_sign(4) == -4
assert reverse_sign(-5) == 5
assert reverse_sign(positive_odd_number) == positive_odd_number * -1
assert reverse_sign(positive_even_number) == positive_even_number * -1
assert reverse_sign(negative_odd_number) == negative_odd_number * -1
assert reverse_sign(negative_even_number) == negative_even_number * -1
print("Exercise 24 is correct.")

# Exercise 25
# Write a function definition named absolute_value that takes in a number and returns the absolute value of the provided number

def absolute_value(number):
    return abs(number)
    # return number if number >= 0 else -number

assert absolute_value(4) == 4
assert absolute_value(-5) == 5
assert absolute_value(positive_odd_number) == positive_odd_number
assert absolute_value(positive_even_number) == positive_even_number
assert absolute_value(negative_odd_number) == negative_odd_number * -1
assert absolute_value(negative_even_number) == negative_even_number * -1
print("Exercise 25 is correct.")

# Exercise 26
# Write a function definition named is_multiple_of_three that takes in a number and returns True or False if the number is evenly divisible by 3.

def is_multiple_of_three(number):
    return True if number % 3 == 0 else False

assert is_multiple_of_three(3) == True
assert is_multiple_of_three(15) == True
assert is_multiple_of_three(9) == True
assert is_multiple_of_three(4) == False
assert is_multiple_of_three(10) == False
print("Exercise 26 is correct.")

# Exercise 27
# Write a function definition named is_multiple_of_five that takes in a number and returns True or False if the number is evenly divisible by 5.

def is_multiple_of_five(number):
    return True if number % 5 == 0 else False

assert is_multiple_of_five(3) == False
assert is_multiple_of_five(15) == True
assert is_multiple_of_five(9) == False
assert is_multiple_of_five(4) == False
assert is_multiple_of_five(10) == True
print("Exercise 27 is correct.")

# Exercise 28
# Write a function definition named is_multiple_of_both_three_and_five that takes in a number and returns True or False if the number is evenly divisible by both 3 and 5.

def is_multiple_of_both_three_and_five(number):
    return True if number % 3 == 0 and number % 5 == 0 else False

assert is_multiple_of_both_three_and_five(15) == True
assert is_multiple_of_both_three_and_five(45) == True
assert is_multiple_of_both_three_and_five(3) == False
assert is_multiple_of_both_three_and_five(9) == False
assert is_multiple_of_both_three_and_five(4) == False
print("Exercise 28 is correct.")

# Exercise 29
# Write a function definition named square that takes in a number and returns the number times itself.
def square(number):    
    # https://www.freecodecamp.org/news/how-to-square-a-number-in-python-squaring-function/
    # more optimized because ** is an operator, which doesn't have overhead
    return number ** 2
    # less optimized because pow() is a function that has slight overhead
    # return pow(number, 2)

assert square(3) == 9
assert square(2) == 4
assert square(9) == 81
assert square(positive_odd_number) == positive_odd_number * positive_odd_number
print("Exercise 29 is correct.")

# Exercise 30
# Write a function definition named add that takes in two numbers and returns the sum.
def add(number1, number2):
    return number1 + number2

assert add(3, 2) == 5
assert add(10, -2) == 8
assert add(5, 7) == 12
print("Exercise 30 is correct.")

# Exercise 31
# Write a function definition named cube that takes in a number and returns the number times itself, times itself.
def cube(number):
    return number*number*number

assert cube(3) == 27
assert cube(2) == 8
assert cube(5) == 125
assert cube(positive_odd_number) == positive_odd_number * positive_odd_number * positive_odd_number
print("Exercise 31 is correct.")

# Exercise 32
# Write a function definition named square_root that takes in a number and returns the square root of the provided number

def square_root(number):
    # https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python
    # Time for the '** (1/2)' method: 0.072819388
    # Time for the 'math.sqrt'method: 0.07792035
    # fractional square (more optimized)
    return number ** (1/2)
    # math.sqrt method (less optimized)
    # return math.sqrt(9)

assert square_root(4) == 2.0
assert square_root(64) == 8.0
assert square_root(81) == 9.0
print("Exercise 32 is correct.")

# Exercise 33
# Write a function definition named subtract that takes in two numbers and returns the first minus the second argument.
def subtract(number1, number2):
    return number1 - number2

assert subtract(8, 6) == 2
assert subtract(27, 4) == 23
assert subtract(12, 2) == 10
print("Exercise 33 is correct.")

# Exercise 34
# Write a function definition named multiply that takes in two numbers and returns the first times the second argument.
def multiply(number1, number2):
    return number1*number2

assert multiply(2, 1) == 2
assert multiply(3, 5) == 15
assert multiply(5, 2) == 10
print("Exercise 34 is correct.")

# Exercise 35
# Write a function definition named divide that takes in two numbers and returns the first argument divided by the second argument.

def divide(number1, number2):
    return number1 / number2

assert divide(27, 9) == 3
assert divide(15, 3) == 5
assert divide(5, 2) == 2.5
assert divide(10, 2) == 5
print("Exercise 35 is correct.")

# Exercise 36
# Write a function definition named quotient that takes in two numbers and returns only the quotient from dividing the first argument by the second argument.
def quotient(number1, number2):
    return number1 // number2

assert quotient(27, 9) == 3
assert quotient(5, 2) == 2
assert quotient(10, 3) == 3
print("Exercise 36 is correct.")

# Exercise 37
# Write a function definition named remainder that takes in two numbers and returns the remainder of first argument divided by the second argument.
def remainder(number1,number2):
    return number1 % number2
assert remainder(3, 3) == 0
assert remainder(5, 2) == 1
assert remainder(7, 5) == 2
print("Exercise 37 is correct.")

# Exercise 38
# Write a function definition named sum_of_squares that takes in two numbers, squares each number, then returns the sum of both squares.
def sum_of_squares(number1, number2):
    return number1**2 + number2**2

assert sum_of_squares(3, 2) == 13
assert sum_of_squares(5, 2) == 29
assert sum_of_squares(2, 4) == 20
print("Exercise 38 is correct.")

# Exercise 39
# Write a function definition named times_two_plus_three that takes in a number, multiplies it by two, adds 3 and returns the result.
def times_two_plus_three(number):
    return number * 2 + 3

assert times_two_plus_three(0) == 3
assert times_two_plus_three(1) == 5
assert times_two_plus_three(2) == 7
assert times_two_plus_three(3) == 9
assert times_two_plus_three(5) == 13
print("Exercise 39 is correct.")

# Exercise 40
# Write a function definition named area_of_rectangle that takes in two numbers and returns the product.
def area_of_rectangle(length, width):
    return length * width

assert area_of_rectangle(1, 3) == 3
assert area_of_rectangle(5, 2) == 10
assert area_of_rectangle(2, 7) == 14
assert area_of_rectangle(5.3, 10.3) == 54.59
print("Exercise 40 is correct.")

# Exercise 41
# Write a function definition named area_of_circle that takes in a number representing a circle's radius and returns the area of the circle
# A = πr^2
def area_of_circle(radius):
    return math.pi * radius ** 2

assert area_of_circle(3) == 28.274333882308138
assert area_of_circle(5) == 78.53981633974483
assert area_of_circle(7) == 153.93804002589985
print("Exercise 41 is correct.")

# Exercise 42
# Write a function definition named circumference that takes in a number representing a circle's radius and returns the circumference.
# C = 2πr
def circumference(radius):
    print(math.pi)
    return 2 * math.pi * radius

assert circumference(3) == 18.84955592153876
assert circumference(5) == 31.41592653589793
assert circumference(7) == 43.982297150257104
print("Exercise 42 is correct.")