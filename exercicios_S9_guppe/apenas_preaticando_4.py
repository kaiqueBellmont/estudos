lista1 = [x for x in range(38, 28, -1)]
# print(lista1)
print(lista1)


lista2 = 'berlin cairo brasil holanda espanha portugual USA mexico japao china'
list(lista2.split())
lista2 = lista2.split()

dicionario = {lista2[i]: lista1[i] for i in range(len(lista1))}
print(dicionario)


