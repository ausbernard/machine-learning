import time
from merge_lists_alt import Merge
from roman_to_int import RomanToInt
from subsequence import SubSequence
from best_time_stock import MaxProfit
from util import Utilities

#### Merge Problem
merge_instance = Merge()
utilities = Utilities()
word1 = utilities.generate_random_string(1000000000)
word2 = utilities.generate_random_string(2000000000)

start_time = time.time()

merged = merge_instance.mergeAlternately(word1, word2)

end_time = time.time()

elapsed_time = end_time - start_time
# Perform assertions
assert merged, "Merged string is empty"
assert len(merged) == len(word1) + len(word2), "Length of merged string is incorrect"
# Check the order of characters in the merged string
for i in range(len(word1)):
    assert merged[2 * i] == word1[i], f"Character {word1[i]} from word1 is not in the correct position"
for i in range(len(word2)):
    assert merged[2 * i + 1] == word2[i], f"Character {word2[i]} from word2 is not in the correct position"
# Print success message
print("All Merge test cases passed!")

#### Roman Int
roman_instance = RomanToInt()
# Test 1
start_time = time.time()
roman_int = roman_instance.GreedyFast("XCVII")
end_time = time.time()
elapsed_time = end_time - start_time
# print(f"answer: {roman_int}")
# print(f"Time taken: {elapsed_time:.6f} seconds")
assert roman_int == 97, f"Expected 97, but got {roman_int}"
# Test 2
start_time = time.time()
roman_int = roman_instance.GreedySlow("XCVII")
end_time = time.time()
elapsed_time = end_time - start_time
# print(roman_int)
# print(f"Time taken: {elapsed_time:.6f} seconds")
# print(f"answer: {roman_int}")  
assert roman_int == 97, f"Expected 97, but got {roman_int}"
print("All RomanInt test cases passed!")


#### Is Subsequence?
subseq = SubSequence()
# Test case 1
s1 = 'abc'
t1 = 'ahbgdc'
output = subseq.isSubsequence(s1, t1)
assert output == True, f"Expected True, but got {output}"
# Test case 2
s2 = 'axc'
t2 = 'ahbgdc'
output = subseq.isSubsequence(s2, t2)
assert output == False, f"Expected False, but got {output}"
print("All SubSequence test cases passed!")

#### Max Profit
mp = MaxProfit()
# test case 1
prices = [2,4,1]
max_prof = mp.maxProfit(prices)
assert max_prof == 2, f"Expected 2, but got {max_prof}"
# test case 2
prices = [7, 6, 4, 3, 1]
max_prof = mp.maxProfit(prices)
assert max_prof == 0, f"Expected 0, but got {max_prof}"
# test case 3
prices = [1, 2, 3, 4, 5]
max_prof = mp.maxProfit(prices)
assert max_prof == 4, f"Expected 4, but got {max_prof}"
# test case 4
prices = [2,4,1]
max_prof = mp.maxProfit(prices)
assert max_prof == 2, f"Expected 2, but got {max_prof}"
# test case 5
prices = []
max_prof = mp.maxProfit(prices)
assert max_prof == 0, f"Expected 0, but got {max_prof}"
# test case 6
prices = [44, 34, 64, 19, 40, 87, 15, 54, 31, 90, 47, 75, 100, 30, 59, 72, 75, 58, 22, 81, 94, 76, 19, 66, 21, 38, 27, 92, 58, 37, 29, 51, 43, 97, 74, 57, 76, 34, 57, 68, 34, 42, 41, 63, 77, 99, 47, 83, 53, 98, 62, 14, 67, 75, 64, 86, 47, 53, 5, 68, 9, 3, 76, 23, 89, 6, 80, 27, 52, 64, 42, 6, 41, 5, 91, 42, 35, 60, 92, 88, 65, 74, 25, 98, 86, 20, 40, 21, 82, 80, 13, 73, 82, 6, 80, 23, 6, 42, 25, 59, 31, 28, 6, 85, 35, 76, 45, 49, 38, 28, 16, 83, 6, 52, 6, 93, 62, 4, 44, 74, 75, 71, 46, 86, 42, 25, 96, 64, 20, 99, 80, 14, 45, 39, 67, 1, 91, 64, 88, 18, 17, 74, 69, 64, 78, 23, 99, 43, 53, 49, 34, 26, 13, 49, 56, 96, 17, 58, 63, 61, 72, 32, 56, 4, 10, 13, 17, 88, 38, 48, 25, 17, 27, 71, 34, 28, 49, 10, 99, 51, 74, 95, 45, 79, 35, 16, 21, 14, 69, 80, 26, 21, 100, 1, 54, 90, 100, 44, 4, 83, 27, 55, 48, 2, 91, 99, 60, 71, 83, 92, 56, 6, 90, 75, 1, 78, 58, 31, 53, 22, 80, 60, 67, 36, 31, 23, 87, 14, 9, 100, 95, 60, 15, 12, 45, 98, 51, 81, 90, 62, 5, 79, 82, 5, 1, 96, 86, 45, 42, 61, 61, 44, 33, 35, 78, 26, 63, 45, 40, 77, 48, 40, 63, 54, 7, 95, 50, 57, 71, 33, 43, 25, 46, 45, 1, 64, 77, 43, 74, 16, 29, 8, 73, 93, 34, 5, 50, 23, 26, 44, 85, 83, 97, 27, 14, 94, 20, 41, 19, 2, 62, 80, 94, 48, 22, 95, 1, 16, 100, 7, 11, 25, 70, 12, 3, 33, 100, 60, 99, 33, 40, 54, 18, 2, 3, 38, 12, 65, 96, 18, 41, 77, 100, 84, 49, 56, 22, 48, 61, 61, 75, 25, 17, 97, 39, 21, 43, 43, 43, 99, 14, 34, 91, 37, 22, 93, 68, 4, 15, 57, 77, 74, 33, 86, 77, 84, 63, 28, 50, 22, 37, 51, 83, 79, 95, 73, 80, 93, 56, 90, 69, 95, 44, 24, 43, 82, 57, 42, 99, 82, 50, 78, 96, 64, 33, 12, 33, 63, 92, 48, 89, 86, 56, 12, 69, 23, 42, 66, 13, 79, 13, 2, 19, 36, 57, 5, 38, 95, 70, 95, 70, 36, 93, 71, 48, 83, 22, 6, 62, 91, 80, 7, 4, 68, 50, 70, 12, 89, 56, 12, 10, 32, 58, 78, 91, 98, 55, 91, 19, 8, 54, 53, 1, 97, 90, 52, 92, 100, 22, 71, 29, 92, 4, 84, 48, 46, 54, 97, 17, 84, 92, 47, 9, 87, 5, 93, 60, 40, 50, 44, 61, 14, 61, 68, 5, 58, 87, 86, 70, 9, 80, 68, 73, 10, 91, 94, 25, 89, 74, 79, 20, 8, 94, 29, 63, 90, 33, 9, 36, 48, 29, 53, 19, 35, 49, 37, 58, 30, 19, 100, 81, 13, 62, 89, 6, 6, 17, 62, 14, 12, 19, 51, 58, 12, 63, 5, 59, 23, 70, 68, 25, 94, 93, 20, 41, 76, 42, 61, 85, 18, 65, 3, 75, 11, 40, 94, 88, 79, 40, 16, 91, 51, 32, 100, 41, 6, 83, 34, 18, 94, 92, 46, 25, 5, 16, 96, 74, 12, 31, 10, 48, 76, 88, 52, 74, 27, 74, 43, 85, 15, 31, 64, 8, 17, 48, 83, 39, 17, 10, 88, 23, 52, 14, 3, 52, 47, 61, 3, 89, 46, 43, 29, 19, 29, 52, 32, 95, 1, 53, 92, 15, 61, 77, 43, 98, 23, 71, 26, 20, 86, 27, 24, 77, 22, 28, 71, 28, 86, 10, 21, 9, 23, 83, 47, 26, 39, 82, 69, 30, 25, 9, 49, 93, 48, 39, 44, 85, 9, 81, 77, 70, 52, 16, 77, 70, 62, 94, 46, 31, 60, 33, 96, 64, 89, 40, 85, 36, 7, 40, 43, 19, 19, 30, 38, 4, 82, 63, 89, 5, 69, 92, 66, 85, 51, 85, 75, 7, 25, 97, 82, 40, 41, 83, 79, 68, 32, 90, 30, 18, 57, 48, 61, 6, 46, 3, 45, 78, 93, 92, 63, 17, 45, 81, 56, 81, 23, 29, 19, 93, 76, 16, 97, 35, 55, 3, 22, 28, 56, 27, 29, 79, 74, 43, 16, 39, 29, 17, 9, 83, 90, 19, 19, 52, 40, 77, 52, 44, 2, 65, 1, 10, 76, 76, 85, 97, 29, 23, 1, 100, 35, 18, 85, 85, 59, 70, 32, 45, 7, 84, 24, 27, 79, 61, 44, 70, 100, 9, 87, 99, 22, 11, 34, 29, 44, 95, 21, 74, 63, 56, 55, 61, 49, 40, 38, 18, 6, 2, 31, 67, 21, 20, 22, 73, 64, 61, 97, 23, 78, 13, 92, 64, 20, 9, 41, 94, 69, 52, 29, 97, 16, 91, 49, 70, 78, 77, 8, 81, 44, 45, 1, 34, 68, 9, 72, 35, 73, 55, 61, 69, 37, 73, 63, 91, 78, 71, 35, 12, 30, 75, 73, 33, 47, 61, 65, 92, 36, 32, 34, 71, 86, 40, 96, 41, 6, 26, 10, 66, 50, 64, 84, 35, 25, 47, 92, 96, 53, 80, 82, 83, 57, 22, 46, 86, 32, 71, 88, 11, 47, 50, 61, 9, 31, 42, 98, 62, 74, 9, 79, 74, 1, 2, 98, 21, 99, 41, 25, 1, 82, 22, 42, 53, 42, 50, 50, 60, 50, 52, 86, 22, 90, 83, 94, 81, 72, 54, 22, 31, 78, 56, 89, 87, 49, 15, 12, 80, 60, 43, 34, 55, 83, 67, 6, 4, 2, 72, 66, 98, 56, 61, 19, 40, 5, 61, 74, 11, 88, 8, 48, 65, 92, 11, 84, 21, 13, 76, 86, 72, 39, 83, 29, 39, 43, 95, 60, 50, 62, 70, 72, 6, 16, 76, 68]
max_prof = mp.maxProfit(prices)
assert max_prof == 99, f"Expected 99, but got {max_prof}"
print("All Max Profit test cases passed!")