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
        return self.__idade

    def print_me(self):
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

    def buscar_por_nome(self, nome):
            for pessoa in self.__pessoas:
                if nome == pessoa.nome:
                    return pessoa
            return "Pessoa não encontrada"

    def printar_pessoas(self):
        for pessoa in self.__pessoas:
            pessoa.print_me()
            print("____________________________________________")


agenda = Agenda()
kaique = Pessoa(nome='kaique', idade=24, altura=1.83)
elias = Pessoa(nome='Elias', idade=33, altura=1.50)
henrrique = Pessoa(nome='Henrrique', idade=35, altura=1.65)

agenda.adicionar_pessoa(kaique)
agenda.adicionar_pessoa(henrrique)
agenda.printar_pessoas()



