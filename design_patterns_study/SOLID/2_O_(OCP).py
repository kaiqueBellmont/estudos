# 2) O princípio aberto-fechado (OCP)

"""
“ Entidades de software ... devem ser abertas para extensão, mas fechadas para modificação”
"""

"""
Em outras palavras: Você não deve precisar modificar o código que já escreveu para acomodar a nova funcionalidade, 
mas simplesmente adicionar o que você precisa agora. 
"""

"""
Isso não significa que você não pode alterar seu código quando as premissas do código precisam ser modificadas, 
mas se você precisar adicionar novas funções semelhantes à presente, você não deve exigir a alteração de outras 
partes do código. 

"""

"""Para esclarecer esse ponto, vamos nos referir ao exemplo que vimos anteriormente. Se quiséssemos adicionar uma 
nova funcionalidade, por exemplo, calcular a mediana, deveríamos ter criado uma nova função de método e adicionar sua 
invocação a “principal”. Isso teria adicionado uma extensão, mas também modificado o principal. 


Podemos resolver isso transformando todas as funções que escrevemos em subclasses de uma classe. Neste caso, 
criei uma classe abstrata chamada “Operações” com um método abstrato “get_operation”. (Classes abstratas geralmente 
são um tópico avançado. Se você não sabe o que é uma classe abstrata, pode executar o código a seguir mesmo sem). 
"""

"""Agora, todas as funções antigas, agora as classes são chamadas pelo método __subclasses __ (). Isso encontrará 
todas as classes herdadas de Operações e operará a função “operações” que está presente em todas as subclasses. 
"""

import numpy as np
from abc import ABC, abstractmethod


class Operations(ABC):
    '''Operations'''

    @abstractmethod
    def operation():
        pass


class Mean(Operations):
    '''Compute Max'''

    def operation(list_):
        print(f"The mean is {np.mean(list_)}")


class Max(Operations):
    '''Compute Max'''

    def operation(list_):
        print(f"The max is {np.max(list_)}")


class Main:
    '''Main'''

    @abstractmethod
    def get_operations(list_):
        # __subclasses__ will found all classes inheriting from Operations
        for operation in Operations.__subclasses__():
            operation.operation(list_)


if __name__ == "__main__":
    Main.get_operations([1, 2, 3, 4, 5])
# The mean is 3.0
# The max is 5

"""Se agora quisermos adicionar uma nova operação ex: mediana, precisaremos apenas adicionar uma classe “Mediana” 
herdada da classe “Operações”. A subclasse recém-formada será imediatamente escolhida por __subclasses __ () e 
nenhuma modificação em qualquer outra parte do código precisa acontecer. O resultado é uma aula muito flexível, 
que requer um tempo mínimo para ser mantida. """