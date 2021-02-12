import uuid


class Pessoa:

    def __init__(self, nome=None, idade=None, altura=None):
        self.__id = uuid.uuid4()
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def id(self):
        return self.__id

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

    def buscar_pessoa_por_nome(self, nome):
        for pessoa in self.__pessoas:
            if nome == pessoa.nome:
                return pessoa
        return None

    def print_pessoas(self):
        for pessoa in self.__pessoas:
            pessoa.print_me()
            print("---------------------------------")


agenda = Agenda()

kaique = Pessoa(nome="Kaique", idade=30, altura=1.68)
henrique = Pessoa(nome="Henrique", idade=34, altura=1.65)

agenda.adicionar_pessoa(kaique)
agenda.adicionar_pessoa(henrique)

agenda.print_pessoas()

pessoa_localizada = agenda.buscar_pessoa_por_nome("Kaique2")

if pessoaLocalizada is not None:
    pessoaLocalizada.print_me()
else:
    print("Pessoa não encontrada...")
