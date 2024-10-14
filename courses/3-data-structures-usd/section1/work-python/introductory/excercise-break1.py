def print_info(a):
    n = len(a) #(1)
    avg = 0.0 #(1)
    for i in range(n): #(n)
        print("Element #%d is %d" % (i,a[i])) 
        avg += a[i] 
    avg /= n #(1)
    print("Average is %f" % avg) #(1)
    
# overall space complexity is O(n)