class Televisao:
    __ultimoVolume = 0
    __canal = None
    __volume = None

    def __init__(self, nome):
        self.__nome = nome
        self.__canal = 1
        self.__volume = 10

    def mostrar_nome(self):
        print(self.__nome)

    def aumentar_volume(self):
        self.__volume += 1
        self.mostrar_volume()

    def diminuir_volume(self):
        self.__volume -= 1
        self.mostrar_volume()

    def mutar(self):
        if self.__ultimoVolume == 0:
            self.__ultimoVolume = self.__volume
            self.__volume = 0
            print('A TV está sem som')
        else:
            self.__volume = self.__ultimoVolume
            self.__ultimoVolume = 0
            self.mostrar_volume()

    def proximo_canal(self):
        self.__canal += 1
        self.mostrar_canal()

    def canal_anterior(self):
        self.__canal -= 1
        self.mostrar_canal()

    def trocar_canal(self, canal):
        self.__canal = canal
        self.mostrar_canal()

    def mostrar_volume(self):
        if self.__volume == 0:
            print('A TV está sem som')
        else:
            print(f'Volume atual: {self.__volume}')

    def mostrar_canal(self):
        print(f'Canal atual: {self.__canal}')


class Controle_remoto:
    def __init__(self):
        self.__tv = tv

    def apontar_para_tv(self, tv=Televisao):
        self.__tv.mostrar_nome()

    def aumentar_volume(self):
        self.__tv.aumentar_volume()

    def diminuir_volume(self):
        self.__tv.diminuir_volume()

    def mutar(self):
        self.__tv.mutar()

    def proximo_canal(self):
        self.__tv.proximo_canal()

    def canal_anterior(self):
        self.__tv.canal_anterior()

    def trocar_canal(self, canal):
        self.__tv.trocar_canal(canal)

    def mostrar_volume(self):
        self.__tv.mostrar_volume()

    def mostrar_canal(self):
        self.__tv.mostrar_canal()

    def informacao(self):
        self.mostrar_volume()
        self.mostrar_canal()


tv1 = Televisao("TV 1")
tv2 = Televisao("TV 2")
controlle = Controle_remoto()
controlle.apontar_para_tv(tv1)
controlle.informacao()
controlle.apontar_para_tv(tv2)
controlle.trocar_canal(25)
controlle.trocar_canal(int(input("Informe o canal: ")))
controlle.apontar_para_tv(tv2)
controlle.informacao()
