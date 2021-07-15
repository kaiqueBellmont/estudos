"""
1) The Single-responsibility principle (SRP)

O princípio de responsabilidade única (SRP)

    “A class should have one, and only one, reason to change”
    “Uma classe deve ter um, e apenas um, motivo para mudar”


    In other words, every component of your code (in general a class, but also a function) should have one and only
    one responsibility. As a consequence of that, there should be only a reason to change it.

    Em outras palavras, cada componente do seu código (em geral uma classe, mas também uma função) deve ter uma e
    apenas uma responsabilidade . Como consequência disso, deve haver apenas uma razão para alterá-lo.


    Too often you see a piece of code that takes care of an entire process all at once. I.e., A function that loads
    data, modifies and, plots them, all before returning its result.

    Freqüentemente, você vê um pedaço de código que cuida de um processo inteiro de uma vez. Ou seja, uma função que
    carrega dados, os modifica e os plota, tudo antes de retornar seu resultado.


    Let’s take a simpler example, where we have a list of number L = [n1, n2, …, nx] and we compute some mathematical
    functions to this list. For example, compute the mean, median, etc.

    Vamos dar um exemplo mais simples, onde temos uma lista de números L = [n1, n2, ..., nx] e calculamos algumas
    funções matemáticas para essa lista. Por exemplo, calcule a média, mediana, etc.

    A bad approach would be to have a single function doing all the work:
    Uma má abordagem seria ter uma única função fazendo todo o trabalho:

    """
import numpy as np


def math_operations(list_):
    # Compute Average
    print(f"the mean is {np.mean(list_)}")
    # Compute Max
    print(f"the max is {np.max(list_)}")


math_operations(list_=[1, 2, 3, 4, 5])
# the mean is 3.0
# the max is 5

"""A primeira coisa que devemos fazer, para tornar isso mais compatível com SRP, é dividir a função math_operations 
em funções atômicas ! Assim, quando a responsabilidade de uma função não pode ser dividida em mais subpartes. 

O segundo passo é fazer uma única função (ou classe), genericamente chamada de “principal”. Isso chamará todas as 
outras funções uma a uma em um processo passo a passo. """


def get_mean(list_):
    '''Compute Max'''
    print(f"the mean is {np.mean(list_)}")


def get_max(list_):
    '''Compute Max'''
    print(f"the max is {np.max(list_)}")


def main(list_):
    # Compute Average
    get_mean(list_)
    # Compute Max
    get_max(list_)


main([1, 2, 3, 4, 5])
# the mean is 3.0
# the max is 5

"""Agora, você teria apenas um único motivo para alterar cada função conectada com “principal”. O resultado dessa 
ação simples é que agora: É mais fácil localizar erros. Qualquer erro na execução apontará para uma seção menor de 
seu código, acelerando sua fase de depuração. 

Qualquer parte do código é reutilizável em outra seção do seu código. Além disso, e muitas vezes esquecido, 
é mais fácil criar testes para cada função de seu código. Observação lateral sobre o teste: você deve escrever testes 
antes de realmente escrever o script. Porém, isso é freqüentemente ignorado em favor da criação de algum resultado 
interessante para ser mostrado aos interessados. 

Isso já é uma melhoria muito maior em relação ao primeiro exemplo de código. Mas, ter criado uma função “principal” e 
de chamada com responsabilidade única não é o cumprimento total do princípio SR. 

Na verdade, o nosso “principal” tem muitos motivos para ser mudado. A classe é realmente frágil e difícil de manter.
"""