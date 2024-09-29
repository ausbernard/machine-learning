def dist(a):
    n = len(a) #(1)
    for i in range(n-1): #(n - 1 times)
        for j in range(i+1, n): #(depends on i - outter loop)
            print("%d - %d = %d" % (a[j], a[i], a[j]-a[i]))
            
# total iterations is (n-1) + (n-2) + (n-3) ... + 1
# (n^2 - n)/2. --> n^2.