"""
a = int(input())
b = int(input())
a1 = a + 1
for i in range(a1, b):
    a1 += i
    print(i)
print(a1)


teste = list()
a = 1
b = 7
for i in range(a+1, b):
    teste.append(i)

print(sum(teste))
"""


def soma_intervalo(a, b):
    global lista
    for i in range(a+1, b):
        lista.append(i)
    return sum(lista)


lista = list()
numero1 = int(input("Digite o primeiro numero : "))
numero2 = int(input("Digite o segundo numero : "))

print(f'A soma dos numeros entre {numero1} e {numero2} = : {soma_intervalo(numero1, numero2)}')
print(*lista, sep=" + ")



