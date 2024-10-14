import string
import random

class Utilities:
    def generate_random_string(self, length):
        return ''.join(random.choices(string.ascii_letters, k=length))
    
    def generate_random_list(self, length, min_value=1, max_value=100):
        return [random.randint(min_value, max_value) for _ in range(length)]