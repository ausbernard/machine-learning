def oldest_person(population):
    oldest_age = -1
    oldest_names = []
    for person in population: #(n)
        if person.age > oldest_age:
            oldest_age = person.age # set the new oldest age
            oldest_names.clear() #clear the list
            oldest_names.append(person.name) # add the persons name to the oldest_name list
        else:
            if person.age == oldest_age:
                oldest_names.append(person.name)
    return oldest_names

# f(n)=O(n) time complexity which is polynomial time. this can be *solved* so it would fall into the P classification

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# create a population dataset
population = [
    Person("Alice", 30),
    Person("Bob", 40),
    Person("Charlie", 25),
    Person("David", 40),
    Person("Eve", 35)
]

# Test the oldest_person function:
oldest_names = oldest_person(population)
# print(f"Oldest person(s): {oldest_names}")

assert oldest_names == ["Bob", "David"], f"Expected ['Bob', 'David'], but got {oldest_names}"
# Print statement for passing
print("✅Test passed: Oldest person(s) are correctly identified as ['Bob', 'David']")