"""
lista = []
lista_final = []
lista_definitiva = {}
for n in range(100):
    if n % 7 == 0:
        lista.append(n * n)
    else:
        lista.append(n)
lista_definitiva = set(lista) - set(lista_final)
print(lista)
print(lista_final)
print(lista_definitiva)


"""
lista = list(range(129))
lista_definitiva = []
indice = 0
while indice < len(lista):
    lista_definitiva.append(indice)
    indice = indice + 1
    if indice % 7 == 0:
        indice = indice + 1

for n in lista_definitiva:
    if n % 10 == 7:
        lista_definitiva.remove(n)


print(lista_definitiva)
print(len(lista_definitiva))