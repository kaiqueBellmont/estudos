class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def altura(self):
        return self.__altura

    @nome.setter
    def nome(self):
        return self.__nome

    @idade.setter
    def idade(self):
        return self.__idade

    @altura.setter
    def altura(self):
        return self.__altura

    def dados(self):
        print(f'Nome : {self.__nome}')
        print(f'Idade: {self.__idade}')
        print(f'Altura: {self.__altura}')


p1 = Pessoa('kaique', 24, 1.83)
p1.dados()
print(p1.nome)
print(p1.idade)
print(p1.altura)
print(p1.__dict__)
print(Pessoa.__dict__)
del p1.nome
print(p1.__dict__)
