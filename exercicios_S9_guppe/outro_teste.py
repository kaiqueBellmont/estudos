"""
lista = [1, 2, 3, 4, 5]

print(lista)
print(*lista)
print(sum(lista))
res = 'kaique%costa%outro'
print(res.split("%"))

lista = [int(input())for n in range(10)]
print(lista)

lista2 = [n for n in range(100)]
lista3 = [n for n in lista2 if n % 2 == 1]
lista4 = [n for n in lista3 if n % 7 == 0]
print(*lista4)

"""
lista5 = [n for n in range(1, 100)]
lista6 = [n + (n * n + 1) if n % 2 == 0 else n * n * - 1 for n in lista5]
print(lista6)
# exemplo : res = {num: ('par' if num % 2 == 0 else 'impar') for num in casos}
"""
res = {valor: ('positivo' if valor > 0 else 'negativo') for valor in lista6}
print(res)

lista7 = sum(lista6)
if lista7 > 0:
    print(f'Positivado com Saldo {lista7}')
else:
    print(f'Negativado com debito {lista7}')


chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
dicionario = {chaves[i]: valores[i] for i in range(0, len(chaves))}
dicionario2 = {chaves[i]: valores[i] * 2 for i in range(0, len(chaves))}
print(dicionario2)


valores = ['kaique', 'ashiley', 'roberto']
chaves = [n for n in range(len(valores))]
dicionario3 = {chaves[i]: valores[i] for i in range(len(chaves))}
print(dicionario3)

"""

lista_String = [str(n) for n in range(1, 11)]
valores = lista_String
chaves = [n for n in range(1, 11)]
dicionario4 = {chaves[i]: valores[i] for i in range(len(chaves))}
print(dicionario4)
