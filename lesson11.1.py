def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

generate = fib()
for i in range(100):
    print(next(generate))