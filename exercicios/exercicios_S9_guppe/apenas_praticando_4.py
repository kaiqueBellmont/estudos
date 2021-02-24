""""
lista1 = [x for x in range(38, 28, -1)]
# print(lista1)
print(lista1)


lista2 = 'berlin cairo brasil holanda espanha portugual USA mexico japao china'
list(lista2.split())
lista2 = lista2.split()

dicionario = {lista2[i]: lista1[i] for i in range(len(lista1))}
print(dicionario)

numbers = [x for x in range(10)]
quadrado = lambda x: x ** 2
print(list(map(quadrado, numbers)))
print(quadrado(10))

"""
paises = "Brasil CHINA japão USA"
paises = paises.split()
casos = [x for x in range(2, 6)]
print(paises)
paises_e_casos = zip(paises, casos)
print(list(paises_e_casos))
"""
a = [2,3,4]
b = [5,6,7]
c = map(lambda x,y:(x,y),a,b)
"""
# isso aqui é muito importante
paises_e_casos2 = map(lambda x, y: (x, y), paises, casos)
atualizando_casos = lambda dado: (dado[0], dado[1] + 2 ** 7 if dado[1] == 0 else dado[1] ** 8)
novos_casos = list(map(atualizando_casos, paises_e_casos2))
print(f'Novos casos confirmados : {novos_casos}')





