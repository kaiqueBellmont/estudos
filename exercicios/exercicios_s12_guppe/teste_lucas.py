def fatorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n = n - 1
    return resultado


print(fatorial(5))
