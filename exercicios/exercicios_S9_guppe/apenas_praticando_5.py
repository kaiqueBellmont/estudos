"""
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)
print(list(res))

"""


def split(string):
    return string.split(' ')


nomes = 'kaique, nice, paula, carlos, fernande'
lista_nomes = split(nomes)
print(lista_nomes)

print(list(filter(lambda nome: nome[0] == 'k' or nome[-1] == 'e', lista_nomes)))
