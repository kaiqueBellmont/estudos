class Pessoa:

    contador = 1

    def __init__(self, nome, idade, altura):
        self.id = contador
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        Pessoa.contador = Pessoa.contador + 1

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


class Agenda(Pessoa):

    pessoas = []

    def __init__(self, nome, idade, altura):
        super().__init__(nome, idade, altura)

    def armazena_pessoas(self, nome, idade, altura):
        pessoa = Pessoa(nome, idade, altura)
        Agenda.pessoas.append(pessoa)



agenda.armazena_pessoas('kaique', 24, 1.38)



