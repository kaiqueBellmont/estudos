tamanho = 10
conjunto1 = {input(f'Digite um valor numerico para o conjunto 1 (restante:({tamanho - valor}) : ')
             for valor in range(tamanho)}
conjunto2 = {input(f'Digite um valor numerico para o conjunto 2 (restante:({tamanho - valor}) : ')
             for valor in range(tamanho)}

intersection = conjunto1.intersection(conjunto2)
print(f'Conjunto 1 : {sorted(conjunto1)}')
print(f'Conjunto 2 : {sorted(conjunto2)}')
print(f'Numeros comuns nos dois conjuntos : {sorted(intersection)}')
