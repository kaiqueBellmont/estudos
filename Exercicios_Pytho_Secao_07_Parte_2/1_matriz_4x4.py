"""
matriz = list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
z = 0
lista2 = list()
for x, y in enumerate(matriz):
    print(x)
    print(y[z])
    lista2.append(y[z])
    z += 1

print(lista2)
matriz.append(lista2)
print(matriz)


MODO 2 :
A = [[[] for i in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        number = int(input("Please Enter Elements of Matrix A:"))
        A[i][j] = number

print(max(A))

"""
import numpy as np

matriz = list()
linha1 = list()
linha2 = list()
valores = list()
for x in range(2):
    valor = int(input("Diite o numero"))
    linha1.append(valor)
    if valor > 10:
        valores.append(valor)

for x in range(2):
    valor = int(input("Diite o numero"))
    linha2.append(valor)
    if valor > 10:
        valores.append(valor)

matriz.append(linha1)
matriz.append(linha2)
print(np.matrix(matriz))
for i in range(2):
    for j in range(2):
        print(matriz[i][j], end=" ")
    print()
print(valores)

