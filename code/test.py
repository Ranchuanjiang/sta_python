def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


g = fib()
for i in range(10):
    print(next(g))
