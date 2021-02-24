a = int(input("Digite o valor de a : "))
b = int(input("Digite o valor de b : "))

vetor_a = list()
vetor_b = list()

if a < 10000 and b < 10000:
    a = str(a)
    b = str(b)
    for valor_a in a:
        vetor_a.append(int(valor_a))
    vetor_a.sort()
    for valor_b in b:
        vetor_b.append(int(valor_b))
    print(f'A soma de {vetor_a} + {vetor_b} é {sum(vetor_a) + sum(vetor_b)}')
else:
    print('Valores informados incorretamente. ')
