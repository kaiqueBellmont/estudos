def conta_ate(valor_max):
    contador = 1
    while contador <= valor_max:
        yield contador
        contador = contador + 1


print(list(conta_ate(15)))

# fibonacci :


def fibonacci_gen(max):
    a, b ,contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


for n in fibonacci_gen(10):
    print(n)
