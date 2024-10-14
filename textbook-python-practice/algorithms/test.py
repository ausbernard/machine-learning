def fiz_buzz(n):
    for i in range(1, n+1):
        print("Fizzbuzz" if i % 3 == 0 and i % 5 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else i)
fiz_buzz(40)