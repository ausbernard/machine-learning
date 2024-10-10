import time
from merge_lists_alt import Merge
from roman_to_int import RomanToInt

#### Merge Problem

# merge_instance = Merge()
# word1 = merge_instance.generate_random_string(3)
# word2 = merge_instance.generate_random_string(3)

# start_time = time.time()

# merged = merge_instance.mergeAlternately(word1, word2)

# end_time = time.time()

# elapsed_time = end_time - start_time
# print(f"Word 1: {word1}")
# print(f"Word 2: {word2}")
# print(f"Merged string: {merged}")
# print(f"Time taken: {elapsed_time:.6f} seconds")

#### Roman Int
roman_instance = RomanToInt()
# Test 1
start_time = time.time()
roman_int = roman_instance.GreedyFast("MMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIII")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"answer: {roman_int}")
print(f"Time taken: {elapsed_time:.6f} seconds")
assert roman_int == 31104, f"Expected 31104, but got {roman_int}"

# Test 2
start_time = time.time()
roman_int = roman_instance.GreedySlow("MMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIIIMMMDCCCLXXXVIII")
end_time = time.time()
elapsed_time = end_time - start_time
print(roman_int)
print(f"Time taken: {elapsed_time:.6f} seconds")
print(f"answer: {roman_int}")  
assert roman_int == 31104, f"Expected 31104, but got {roman_int}"