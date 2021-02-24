lista1 = [i * i for i in range(1, 10)]
for i in lista1:
    print(i)

pares = [i for i in range(10) if i % 2 == 0]
print(pares)
impares = [i + 1 for i in pares]
print(impares)


def quadrado(valor):
    return valor * valor


quadrado_impares = [quadrado(numero) for numero in impares]
print(quadrado_impares)


quantidade_amigos = int(input("Digite quantos amigos você tem : "))
amigos = [str(input("Digite o nome dos amigos : ")) for amigo in range(quantidade_amigos)]


def teste(nome):
    return nome.title()


nomes_maiusculos = [teste(amigo) for amigo in amigos]
print(nomes_maiusculos)

# nomes_maiusculos = [amigo.title() for amigo in amigos]
# print(nomes_maiusculos)
