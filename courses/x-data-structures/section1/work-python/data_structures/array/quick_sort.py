import array

my_array = array.array('i', [-5,3,2,1,-3,-3,7,9,2])  # 'i' indicates an array of integers

def quick_sort_alg(arr):
    # Time: O(n log n) (Average case, technically Worst case is O(n^2))
    # Space: O(n)
    if len(arr) <= 1:
        return arr
    
    p = arr[-1]
    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]
    
    L = quick_sort_alg(L)
    R = quick_sort_alg(R)
    
    return L + [p] + R
    

print(quick_sort_alg(my_array))