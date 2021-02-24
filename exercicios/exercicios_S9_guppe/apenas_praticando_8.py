texto = 'Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa,' \
        ' orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em'

texto = texto.split()
filto = filter(lambda palavra: palavra[-1] == 'a', texto)
print(list(filto))
filto2 = filter(lambda palavra: len(palavra) < 5, texto)
print(sorted(list(filto2)))

print(type(texto))
lista3 = [len(x) for x in texto]
print(lista3)

elevando = lambda x: (x ** (x - x/2)).__round__(2)
teste_final = map(elevando, lista3)

print(list(teste_final))

texto2 = 'Neste Guia Completo você encontrará todo o conteúdo ' \
         'que precisa para começar a programar com a linguagem Python. Saiba mais sobre Python agora!'
texto2 = texto2.split()
texto_filtrado2 = filter(lambda palavra: palavra[0] == 'a' or palavra[0] == 'p', texto2)
print(list(texto_filtrado2))


lista4 = [x + x ** x for x in range(10)]
print(lista4)
filto3 = filter(lambda x: 300 < x < 50000, lista4)
print(list(filto3))

lista5 = [x for x in range(1, 100, 3)]
teste_final_do_nal = map(lambda x: x if x % 2 == 0 else None, lista5)
teste_final_do_nal2 = filter(None, teste_final_do_nal)
print(list(teste_final_do_nal2))
