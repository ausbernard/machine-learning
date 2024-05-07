def print_info(a):
    n = len(a) #constant time operation - printing a single number (1)
    avg = 0.0
    for i in range(n):
        print(f"Element #{i} is {a[i]}") # 1 operation
        avg += a[i]
    avg /= n # <--- 1
    print("Average is %f" % avg) # <---- 1
    
# f(n) =  2(n) + 3
# O(n)
    