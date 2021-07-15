def somatorio(n):
    soma = 0
    for i in range(1, n):
        soma += i
    return soma


n = 1000
print(somatorio(n))
