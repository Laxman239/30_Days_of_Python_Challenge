def fib(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a+b
        count += 1

for f in fib(10):
    print(f)