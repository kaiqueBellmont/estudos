# Generators
# Fatorial com generators e reduce
from functools import reduce
"""
#filter
res = filter(lambda x: x % 2 == 0, lista)
print(list(res))
"""
lista = (x for x in range(10, 1, -1))
teste = reduce(lambda x, y: x * y, lista)
print(teste)

# para usar o reversed tem que ser em formato lista ou tem de ser uma string
res2 = list(filter(lambda x: x < 54, (x for x in range(1, 100))))
print(list(reversed(res2)))


"""
PARA se utilizar o filter e maps juntos, o filter deve ser passado como iterável
exemplo:
"""
# Este exemplo foi utilizando lambdas, generators, map e filter na mesma função
res3 = tuple(map(lambda x: f'{x}', filter(lambda x: x % 13 == 0 and x < 667, (x for x in range(1000)))))
print(res3)

