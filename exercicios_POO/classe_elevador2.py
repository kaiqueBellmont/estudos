class Elevador:
    __terreo = 0

    def __init__(self, andar_atual=None, total_andares=None, capacidade=None, quantidade_pessoas=None):
        self.__andar_atual = andar_atual
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__quantidade_pessoas = quantidade_pessoas

    @property
    def andar_atual(self):
        return self.__andar_atual

    @property
    def total_andares(self):
        return self.__total_andares

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def quantidade_pessoas(self):
        return self.__quantidade_pessoas

    @andar_atual.setter
    def andar_atual(self, novo_andar):
        self.__andar_atual = novo_andar

    @total_andares.setter
    def total_andares(self, quantidade_andares):
        self.__total_andares = quantidade_andares

    @capacidade.setter
    def capacidade(self, nova_capacidade):
        self.capacidade = nova_capacidade

    @quantidade_pessoas.setter
    def quantidade_pessoas(self, quantidade_nova):
        self.quantidade_pessoas = quantidade_nova

    def print_me(self):
        print(f'Andar atual : {self.__andar_atual}')
        print(f'Capacidade : {self.__capacidade}')
        print(f'Lotação : {self.__quantidade_pessoas}')
        print(f'Andares restantes : {self.__total_andares - self.__andar_atual} ')
        print("__________________________________________________________________________")

    # ESSA função deve ser chamada primeiro
    def inicializa(self, andar_atual=1, total_andares=int(input("Quantos andares tem o prédio? ")),
                   capacidade=int(input("Qual a capacidade do elevador ? ")),
                   quantidade_pessoas=0):
        """
        :param andar_atual: mostra o andar em que está
        :param total_andares: Total de andares do prédio
        :param capacidade: Capacidade total do elevador
        :param quantidade_pessoas: Quantidade de pessoas no elevador
        :return: inicializa o elevador
        """
        self.__andar_atual = andar_atual
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__quantidade_pessoas = quantidade_pessoas

    def entra(self):
        self.__quantidade_pessoas += 1
        if self.__quantidade_pessoas > self.__capacidade:
            print("Capacidade de pessoas excedida")

    def sai(self):
        self.__quantidade_pessoas -= 1
        if self.__quantidade_pessoas < 0:
            print("O elevador já está vazio")

    def informacoes(self):
        elevador.print_me()

    def sobe(self):
        self.__andar_atual += 1
        if self.__andar_atual > self.__total_andares:
            print(f'Impossivel subir mais do que {self.__total_andares} andares.')

    def desce(self):
        self.__andar_atual -= 1
        if self.__andar_atual < Elevador.__terreo:
            print("O Elevador já se encontra no Térreo.")


elevador = Elevador()
elevador.inicializa()
elevador.informacoes()
elevador.sobe()
elevador.informacoes()





