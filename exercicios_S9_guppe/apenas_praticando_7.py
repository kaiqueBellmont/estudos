# praticando lambdas, funções integradas e filtros
steve = ' Steve Jobs foi demitido da Apple em 1985,' \
        ' após uma série de atritos entre os diretores da empresa e o CEO na época, John Sculley'
steve = steve.split()
print(steve)
# menor_palavra = list(map(lambda palavra: palavra, filter(lambda palavra: len(palavra) < 5, steve)))
# print(menor_palavra)
filtro1 = filter(lambda x: len(x) < 5, steve)


from collections import Counter


teste10 = Counter(steve)
print(teste10)





