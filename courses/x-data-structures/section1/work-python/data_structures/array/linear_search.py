import array

my_array = array.array('i', [1, 2, 3, 4])  # 'i' indicates an array of integers
"""
Type Codes for the array Module
'b': signed char (1 byte)
'B': unsigned char (1 byte)
'u': Unicode character (2 bytes)
'h': signed short (2 bytes)
'H': unsigned short (2 bytes)
'i': signed int (4 bytes)
'I': unsigned int (4 bytes)
'l': signed long (4 bytes)
'L': unsigned long (4 bytes)
'q': signed long long (8 bytes)
'Q': unsigned long long (8 bytes)
'f': float (4 bytes)
'd': double (8 bytes)
"""

def lin_search(value, arr):
    return value in arr
    
print(lin_search(6, my_array))

#Time: O(1)s



