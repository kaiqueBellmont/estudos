import os
from subprocess import call


class Televisao:

    def __init__(self):
        self.__canal = 0
        self.__volume = 0
        self.__canal_atual = 0
        self.__volume_atual = 0

    def aumenta_volume(self):
        self.__volume_atual += 1

    def abaixa_volume(self):
        self.__volume_atual -= 1

    def aumenta_canal(self):
        self.__canal_atual += 1

    def abaixa_canal(self):
        self.__canal_atual -= 1

    def volume_atual(self):
        return self.__volume_atual

    def canal_atual(self):
        return self.__canal_atual

    def ajustar_canal(self):
        self.__canal = input()
        if self.__canal == '-' and self.__canal_atual == 0:
            print("O canal já está no 0")
        elif self.__canal == '-' and self.__canal_atual != 0:
            self.__canal_atual -= 1
        elif self.__canal == '+':
            self.__canal_atual += 1
        elif self.__canal.isnumeric():
            self.__canal_atual = self.__canal
        print(f'Canal : {self.__canal_atual}')

    def ajustar_volume(self):
        self.__volume = input()
        if self.__volume == '-' and self.__volume_atual == 0:
            print("O volume já é 0 ")
        elif self.__volume == '-' and self.__volume_atual != 0:
            self.__volume_atual += 1
        elif self.__volume == '+' and self.__volume_atual == 100:
            print("O volume já está no MAX")
        elif self.__volume == '+' and self.__volume_atual < 100:
            self.__volume_atual += 1
        print(f'Volume: {self.__volume_atual}')

    def informacoes(self):
        os.system('clear')
        print(f'Canal : {self.__canal_atual}')
        print(f'Volume: {self.__volume_atual}')


class Controle_remoto:

    def __init__(self, tv):
        self.__tv = tv

    def controlar_volume(self):
        self.__tv.ajustar_volume()

    def controlar_canal(self):
        self.__tv.ajustar_canal()

    def botao_informacao(self):
        self.__tv.informacoes()


tv = Televisao()
controle = Controle_remoto(tv)
controle.controlar_canal()
controle.controlar_volume()
tv.informacoes()

