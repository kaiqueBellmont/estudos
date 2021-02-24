dicionario = {'brasil': 150, 'jamaica': 99}
lista = [tuple(x) for x in dicionario.items()]
print(lista)
"""
casos_suspeitos = lambda dado: (dado[0], dado[1] if dado[1] < 100 else None)
print(list(map(casos_suspeitos, lista)))
"""
filtro = filter(lambda dado: (dado[1] < 100), lista)
print(list(filtro))


lista1 = [x for x in range(15, 0, -1)]
print(lista1)
# def teste(num):
# return num ** 1/2
# ou
teste1 = lambda x: (x ** 1/2).__round__(2)
res = map(teste1, lista1)
print(list(res))


