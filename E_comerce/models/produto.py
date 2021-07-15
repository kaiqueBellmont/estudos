from utils.helper import formata_moeda


class Produto:

    contador = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__nome: str = nome
        self.__preco: float = preco
        self.__codigo: int = Produto.contador
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nPeço: {self.preco}'


produto = Produto(nome=input("Digite o nome:"), preco=float(input("Digite o preço")))

print(produto)

p2 = Produto('caneta', 3.50)
print(p2)

valor = 1500.00
print(formata_moeda(valor))

