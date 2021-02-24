lista = list(range(6))
print(lista)
#como pode perceber, em listar mesmo que naoe xista uma variavel chamada chave e valor, entende-se que o primeiro
#valor é a chave, o segundo é o valor. Se a lista for composta apenas de de valor,
#entende-se: indice e valor.
for indice, valor in enumerate(lista):
    print(f'Digite o valor do indice{indice}:')
    lista[valor] = int(input())

print(lista)
