# Decorators
# Exemplo:
def testando(funcao):
    def testando2():
        print('vai se fuder')
        funcao()
        print('Filho da puta')

    return testando2


@testando
def teste3():
    print('kaique')


teste3()


def impar():
    if 10 % 2 == 0:
        return True


def checa_impar():
    if impar:
        print("impar")


@checa_impar
def teste():
    print(impar())
