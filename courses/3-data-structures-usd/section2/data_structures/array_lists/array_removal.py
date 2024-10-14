def remove(array, index):
    # check for valid index -- if not valid return false
    if index < 0 or index >= len(array):
        return False
    print(array)
    # perform the removal algorithm
    array.pop(index)
    
    # if we didn't remove from the very end of the list
    if index < (len(array)):
        # shift all the elements left one slot
        for i in range(index, len(array) - 1):
            array[i] = array[i + 1]
        # remove the last duplicated item
        print(array)
    
# Example usage
array = [1, 2, 3, 4, 5]
index = 2
result = remove(array, index)
print("Result:", result)  # Output: True
print("Updated Array:", array)  # Output: [1, 2, 4, 5]
