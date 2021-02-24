"""
# reduce
from functools import reduce

# fatorial de n até n
comeco = int(input("Digite o começo do seu fatorial : "))
fim = int(input("Digite o fim do seu fatorial : "))
res = reduce(lambda x, y: x * y, [x for x in range(comeco, fim, -1)])
print(res)

"""
