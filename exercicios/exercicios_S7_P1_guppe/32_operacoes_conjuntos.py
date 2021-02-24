tamanho = 5
lista1 = list(range(tamanho))
lista2 = list(range(tamanho))
lista_multiplacacao = list()
lista_soma = list()
lista_diferenca = list()
uniao = list()
intersection = list()
lista1 = [int(input(f'Por favor digite um valor (Sem repetir) para o conjunto 1 :(restante {tamanho - valor}):'))
             for valor in range(tamanho)]
lista2 = [int(input(f'Por favor digite um valor (Sem repetir) para o conjunto 2 :(restante {tamanho - valor}):'))
             for valor in range(tamanho)]

for num1, num2 in zip(lista1, lista2):
    lista_multiplacacao.append(num1 * num2)
for num1, num2 in zip(lista1, lista2):
    lista_soma.append(num1 + num2)
for num1, num2 in zip(lista1, lista2):
    lista_diferenca.append(num1 - num2)

intersection = set(lista1).intersection(set(lista2))
uniao = set(lista1).union(set(lista2))

print(lista1)
print(lista2)
print(lista_soma)
print(lista_diferenca)
print(lista_multiplacacao)
print(uniao)
print(intersection)
