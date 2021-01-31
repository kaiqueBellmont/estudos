class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def dados(self):
        self.__nome = str(input("Digite seu nome : "))
        self.__idade = input("Digite sua idade : ")
        self.__altura = input("Digite sua altura : ")
        return self.__nome, self.__idade, self.__altura


p1 = Pessoa
print(Pessoa.dados(p1))



