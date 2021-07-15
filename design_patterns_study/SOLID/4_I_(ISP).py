# 4) O Princípio de Segregação de Interface (ISP)

"""
“ Muitas interfaces específicas do cliente são melhores do que uma interface de uso geral ”

"""

"""
No concurso de classes, é considerada uma interface, todos os métodos e propriedades “ expostos ”, ou seja, 
tudo com que um usuário pode interagir que pertence a essa classe. 
"""

"""
Nesse sentido, os princípios do SI nos dizem que uma classe deve ter apenas a interface necessária (SRP) e evitar 
métodos que não funcionam ou que não têm razão para fazer parte dessa classe. 
"""

"""
Esse problema surge, principalmente, quando uma subclasse herda métodos de uma classe base de que não precisa.
"""

# Vejamos um exemplo:


from abc import ABC, abstractmethod
import numpy as np


class Mammals(ABC):
    @abstractmethod
    def swim() -> bool:
        print("Can Swim")

    @abstractmethod
    def walk() -> bool:
        print("Can Walk")


class Human(Mammals):
    def swim():
        return print("Humans can swim")

    def walk():
        return print("Humans can walk")


class Whale(Mammals):
    def swim():
        return print("Whales can swim")


"""Para este exemplo, temos a classe abstrata “Mamíferos” que possui dois métodos abstratos: “caminhar” e “nadar”. 
Esses dois elementos pertencerão à subclasse “Humano”, enquanto apenas “nadar” pertencerá à subclasse “Baleia”. 


E, de fato, se executarmos este código, poderíamos ter:
"""

Human.swim()
Human.walk()

Whale.swim()
Whale.walk()

# Humans can swim
# Humans can walk
# Whales can swim
# Can Walk


"""
A subclasse de baleia ainda pode invocar o método “andar”, mas não deveria , e devemos evitá-lo.

A maneira sugerida pelo ISP é criar mais interfaces específicas do cliente em vez de uma interface de uso geral
Portanto, nosso exemplo de código se torna: """

from abc import ABC, abstractmethod


class Walker(ABC):
    @abstractmethod
    def walk() -> bool:
        return print("Can Walk")


class Swimmer(ABC):
    @abstractmethod
    def swim() -> bool:
        return print("Can Swim")


class Human(Walker, Swimmer):
    def walk():
        return print("Humans can walk")

    def swim():
        return print("Humans can swim")


class Whale(Swimmer):
    def swim():
        return print("Whales can swim")


if __name__ == "__main__":
    Human.walk()
    Human.swim()

    Whale.swim()
    Whale.walk()

# Humans can walk
# Humans can swim
# Whales can swim

"""Agora, cada subclasse herda apenas o que precisa, evitando invocar um sub-método fora do contexto (errado). Isso 
pode criar um erro difícil de detectar. 
"""

"""Este princípio está intimamente conectado com os outros e, especificamente, ele nos diz para manter o conteúdo de 
uma subclasse limpo de elementos inúteis para essa subclasse. Isso tem o objetivo final de manter nossas aulas limpas 
e minimizar erros. 
"""

