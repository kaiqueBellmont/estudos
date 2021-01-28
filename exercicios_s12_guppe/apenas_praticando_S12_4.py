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
