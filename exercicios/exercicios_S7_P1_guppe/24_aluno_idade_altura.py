aluno = list(range(4))
indices = list(range(2))
for indice, valor in enumerate(aluno):
    aluno[indice] = int(input("Digite o valor do inice:"))
    aluno[valor] = float(input("Digite a altura"))
    indices.append(aluno[indice])
    

print(max(aluno))

