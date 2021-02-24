lista = list(range(15))
soma_notas = 0
for indice, valor in enumerate(lista):
    print(f'Digite a nota para o aluno {indice + 1}')
    lista[valor] = float(input())
    soma_notas += lista[valor]

media = soma_notas / len(lista)
for indice, valor in enumerate(lista):
    print(f'Aluno {indice} nota {valor}')

print(f'Media da turma: {media:.2f}')
