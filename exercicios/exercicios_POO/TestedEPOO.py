class Pessoa:

    __id = None

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @__id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def altura(self):
        return self.__altura

    def print_me(self):
        print(f'Nome : {self.__nome}')
        print(f'Idade: {self.__idade}')
        print(f'Altura: {self.__altura}')


class Agenda:

    pessoas = list()

    def adicionar_pessoa(self, pessoa=Pessoa):
        self.pessoas.append(pessoa)


