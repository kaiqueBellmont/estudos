# lambdas
"""
calculo = lambda x, y: x + y
print(calculo(10, 10))

pares = lambda x: x if x % 2 == 0 else print(f'{x} é impar')
print(pares(11))


lista0 = [x for x in range(10)]
print(lista0)

teste1 = lambda x: x ** 2 if x % 2 == 0 else x ** -1

for n in range(len(lista0)):
    print(teste1(n))


autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""
import math


def raio_circunferencia(r):
    # Calcula a área de um círculo com raio 'r'.
    return math.pi * (r ** 2)


raios = [x for x in range(1, 101)]
res = [raio_circunferencia(x).__round__(2) for x in raios]
for indice, valor in enumerate(res):
    # print(f'{x}')
    print(indice+1, "=",  valor)


areas = map(raio_circunferencia, raios)
print(areas)

raios_map = list(map(lambda r: math.pi * (r ** 2), raios))

print('com map:')
for indice, valor in enumerate(raios_map):
    print(indice+1, '=', valor.__round__(2))
