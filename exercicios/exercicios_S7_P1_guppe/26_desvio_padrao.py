# Este programa calcula o desvio padrao de 10 Termos usando listas.
import math
# pega os primeiros valores
lista = [float(input(f'Digite o valor para o indice [{i}] : ')) for i in range(10)]

# subtrai a media e eleva ao quadrado
lista2 = list()

soma = 0
for valor in lista:
    soma += valor
media = soma / len(lista)

for valor in lista:
    lista2.append(pow((valor - media), 2))

# soma dos resultados dos quadrados; Divide por N termos - 1; Tira raiz de todos os resultados anteriores;
# encontra o desvio padrão
desvio_padrao = math.sqrt(sum(lista2) / (len(lista) - 1))
print(f'\nSua lista: \n{lista}\nDesvio padrão: {desvio_padrao:.4f}.')

