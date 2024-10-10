# Algorithm: Greedy Algorithm

# Potential Others:
    # Lookup / Search Algorithm - would work if there wasn't the subtraction rule for roman numerals
    # Dynamic Programming - would work if this problem could be broken down into overlapping sub-problems but it's really just one problem
    # Brute Force - we would have to look at every combination which is not efficient or necessary
class RomanToInt:
    def GreedyFast(self, s: str) -> int:
        """_summary_
        Understanding the Problem: The task is to convert a Roman numeral string to an integer. This involves recognizing the rules of Roman numerals, including the subtraction rule (e.g., "IV" is 4).

        Identifying the Core Logic: The core logic involves iterating through the string and applying the rules of Roman numerals. The subtraction rule is key here: if a smaller numeral appears before a larger one, it should be subtracted.

        Optimizing the Approach: The initial approach involved a more complex iteration with multiple conditions. A more efficient way is to iterate through the string in reverse, which simplifies the logic for handling the subtraction rule.

        Implementing the Solution: Using a dictionary to map Roman numerals to their integer values and a loop to iterate through the string, applying the addition and subtraction rules as needed.

        Testing: Adding test cases to ensure the solution works correctly for various inputs.
        """
        # def get_value(char):
        #     if char == 'I':
        #         return 1
        #     elif char == 'V':
        #         return 5
        #     elif char == 'X':
        #         return 10
        #     elif char == 'L':
        #         return 50
        #     elif char == 'C':
        #         return 100
        #     elif char == 'D':
        #         return 500
        #     elif char == 'M':
        #         return 1000
        #     return 0
        roman_num_dict = {
            "I":1,
            "V":5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            value = roman_num_dict[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total
        
    def GreedySlow(self, s: str) -> int: 
        roman_num_dict = {
            "o": 0,
            "I":1,
            "V":5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        s = "o" + s
        total = 0
        a, b = 0, 1
        
        while a < len(s):
            if s[a] == "I" and b < len(s) and (s[b] == "V" or s[b] == "X"):
                total += (roman_num_dict[s[b]] - roman_num_dict[s[a]])
                a += 2
                b += 2
            elif s[a] == "X" and b < len(s) and (s[b] == "L" or s[b] == "C"):
                total += (roman_num_dict[s[b]] - roman_num_dict[s[a]])
                a += 2
                b += 2
            elif s[a] == "C" and b < len(s) and (s[b] == "D" or s[b] == "M"):
                total += (roman_num_dict[s[b]] - roman_num_dict[s[a]])
                a += 2
                b += 2
            else:
                total += roman_num_dict[s[a]]
                a += 1
                b += 1
            
        
        return total

#### Roman Int
roman_instance = RomanToInt()
# Test 1
roman_int = roman_instance.GreedyFast("MMMDCCCLXXXVIIIMMMDCCCLXXXVIII")
print(f"answer: {roman_int}")
# assert roman_int == 31104, f"Expected 31104, but got {roman_int}"