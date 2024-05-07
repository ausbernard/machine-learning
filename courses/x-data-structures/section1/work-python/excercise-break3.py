def tricky(n):
    operations = 0 # <--- O(1)
    while n > 0:
        for i in range(n):
            print("Operations: %d" % operations) # <--- 1
            operations += 1 # <---- 1
        n = int(n/2) # <---- the sum will approach 2

# f(n) = 2(n) when we drop the coefficient we are left with O(n)