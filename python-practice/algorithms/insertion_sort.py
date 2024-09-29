a = [5,2,4,6,1,3]

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        # Move elements of a[0..i-1], that are greater than key, to one position ahead of their current position
        while i >= 0 and key < a[i]:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

# Example usage
a = [12, 11, 13, 5, 6]
sorted_a = insertion_sort(a)
print("Sorted array:", sorted_a)
    