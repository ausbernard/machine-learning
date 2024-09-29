import random
import string


def read_names():
    with open('/Volumes/fd/machine-learning/python-practice/python_one_liners/resources/names/first-names.txt', 'r') as file:
        return file.read().splitlines()
    
def generate_random_names(k=10):
    names = read_names()
    return random.sample(names, k)  # Adjust k to the desired number of names

def generate_random_salary(min_salary=20000, max_salary=300000):
    return random.randint(min_salary, max_salary)

def generate_random_data(num_entries=50):
    data = {}
    names = generate_random_names(num_entries)
    for name in names:
        salary = generate_random_salary()
        data[name] = salary
    return data

# Generate the dictionary with 50 entries
random_data = generate_random_data()

# Print the generated dictionary
print(random_data)
