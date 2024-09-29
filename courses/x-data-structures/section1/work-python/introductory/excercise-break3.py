def tricky(n):
    operations = 0 #(1)
    while n > 0: #(n)
        for i in range(n):
            print("Operations: %d" % operations)
            operations += 1
        n = int(n/2) #(1/2n)

# 1 + 1/2n + 1/4n + 1/8n + 1/16n ... 1. This is 2n. Which is O(n)