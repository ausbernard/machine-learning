# Exercise 43
# Write a function definition named is_vowel that takes in value and returns True if the value is a, e, i, o, u in upper or lower case.

def is_vowel(letter):
    vowel = 'aAeEiIoOuU'
    return True if letter in vowel else False

assert is_vowel("a") == True
assert is_vowel("e") == True
assert is_vowel("i") == True
assert is_vowel("o") == True
assert is_vowel("u") == True
assert is_vowel("A") == True
assert is_vowel("E") == True
assert is_vowel("I") == True
assert is_vowel("O") == True
assert is_vowel("U") == True
assert is_vowel("banana") == False
assert is_vowel("Q") == False
assert is_vowel("y") == False
assert is_vowel("aei") == False
assert is_vowel("iou") == False
print("Exercise 43 is correct.")

# Exercise 44
# Write a function definition named has_vowels that takes in value and returns True if the string contains any vowels.

def has_vowels(letters):
    vowels = set('aAeEiIoOuU')
    #The any() function will return True as soon as it finds a vowel in the input string, and False otherwise.
    return any(letter in vowels for letter in letters)

assert has_vowels("banana") == True
assert has_vowels("ubuntu") == True
assert has_vowels("QQQQ") == False
assert has_vowels("wyrd") == False
print("Exercise 44 is correct.")

# Exercise 45
# Write a function definition named count_vowels that takes in value and returns the count of the number of vowels in a sequence.

def count_vowels(sequence):
    vowels = set('aAeEiIoOuU')
    return sum(1 for letter in sequence if letter in vowels)
    
assert count_vowels("banana") == 3
assert count_vowels("ubuntu") == 3
assert count_vowels("mango") == 2
assert count_vowels("QQQQ") == 0
assert count_vowels("wyrd") == 0
print("Exercise 45 is correct.")

# Exercise 46
# Write a function definition named remove_vowels that takes in string and returns the string without any vowels

def remove_vowels(string):
    vowels = set('aAeEiIoOuU')
    return ''.join(char for char in string if char not in vowels)
    # result = []
    # for char in string:
    #     if char not in vowels:
    #         result.append(char)
    # return ''.join(result)
    # for vowel in vowels:
    #     string = string.replace(vowel,'')
    # return string

assert remove_vowels("banana") == "bnn"
assert remove_vowels("ubuntu") == "bnt"
assert remove_vowels("mango") == "mng"
assert remove_vowels("QQQQ") == "QQQQ"
print("Exercise 46 is correct.")

# Exercise 47
# Write a function definition named starts_with_vowel that takes in string and True if the string starts with a vowel

def starts_with_vowel(string):
    vowels = set('aAeEiIoOuU')
    return string[0] in vowels
    # It has a time complexity of O(1), which means it takes constant time regardless of the size of the input string.
    # if string[0] in vowels:
    #     return True
    # else:
    #     return False

assert starts_with_vowel("ubuntu") == True
assert starts_with_vowel("banana") == False
assert starts_with_vowel("mango") == False
print("Exercise 47 is correct.")

# Exercise 48
# Write a function definition named ends_with_vowel that takes in string and True if the string ends with a vowel

def ends_with_vowel(string):
    vowels = set('aAeEiIoOuU')
    # It has a time complexity of O(1), which means it takes constant time regardless of the size of the input string.
    return string[-1] in vowels

assert ends_with_vowel("ubuntu") == True
assert ends_with_vowel("banana") == True
assert ends_with_vowel("mango") == True
assert ends_with_vowel("spinach") == False
print("Exercise 48 is correct.")

# Exercise 49
# Write a function definition named starts_and_ends_with_vowel that takes in string and returns True if the string starts and ends with a vowel
def starts_and_ends_with_vowel(string):
    vowels = set('aAeEiIoOuU')
    return string[0] in vowels and string[-1] in vowels

assert starts_and_ends_with_vowel("ubuntu") == True
assert starts_and_ends_with_vowel("banana") == False
assert starts_and_ends_with_vowel("mango") == False
print("Exercise 49 is correct.")
