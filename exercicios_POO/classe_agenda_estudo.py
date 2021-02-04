class Pessoa:

    def __init__(self, nome=None, idade=None, altura=None):
        self.__nome = nome
        self.__idade= idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def altura(self):

    def print_me(self):
        print(f'Id : {self.__id}')
        print(f'Nome : {self.__nome}')
        print(f'Idade: {self.__idade}')
        print(f'Altura: {self.__altura}')


class Agenda:
    __pessoas = list()

    def adicionar_pessoa(self, pessoa):
        self.__pessoas.append(pessoa)

    def remover_pessoa(self, nome):
        for pessoa in self.__pessoas:
            if nome == pessoa.nome:
                self.__pessoas.remove(pessoa)
                break


