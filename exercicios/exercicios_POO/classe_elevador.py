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

    def inicializa(self, total_andares, andar_atual):
       self.__total_andares = 10


