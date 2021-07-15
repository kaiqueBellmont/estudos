import math


def soma_quadrados(a, b, c):
    soma_todos = math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2)
    print(f'A Soma dos quadrados = {soma_todos}')
    return soma_todos


print("Digite o valor de a :")
a = input()
a = float(a)

print("Digite o valor de b :")
b = input()
b = float(b)

print("Digite o valor de c :")
c = input()
c = float(c)

soma_quadrados(a, b, c)
