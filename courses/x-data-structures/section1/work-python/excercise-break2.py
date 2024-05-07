def dist(a):
    n = len(a)  # <--- O(1)
    for i in range(n-1): # nested for loops
        for j in range(i+1, n): 
            print("%d - %d = %d" % (a[j], a[i], a[j]-a[i])) # for each element in the list, the function iterates over the remaining element
            
## O(n^2)