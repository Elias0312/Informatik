def fibonacci_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rec(n - 2) + fibonacci_rec(n - 1)
    

for i in range(1, 21):
    print(fibonacci_rec(i))