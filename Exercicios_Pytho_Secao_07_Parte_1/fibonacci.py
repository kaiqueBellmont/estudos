for n in range(20):
    fib = lambda x: x if x<=1 else fib(x-1) + fib(x-2)
    print(f'{n} = {fib(n)}')


