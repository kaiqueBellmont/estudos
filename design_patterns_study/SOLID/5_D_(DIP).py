# 5) O Princípio de Inversão de Dependência (DIP)

"""“ Abstrações não devem depender de detalhes. Os detalhes devem depender da abstração. Módulos de alto nível não
devem depender de módulos de baixo nível. Ambos devem depender de abstrações ”
"""

"""Portanto, essas abstrações (por exemplo, a interface, como visto acima) não devem ser dependentes de métodos de 
baixo nível, mas ambas devem depender de uma terceira interface. Para explicar melhor esse conceito, prefiro pensar 
em uma espécie de fluxo de informações. Imagine que você tenha um programa que recebe um conjunto específico de 
informações (um arquivo, um formato, etc) e você escreveu um script para processá-lo. O que aconteceria se essas 
informações estivessem sujeitas a alterações? Você teria que reescrever seu roteiro e ajustar o novo formato. Perder 
a compatibilidade retro com os arquivos mais antigos. No entanto, você pode resolver isso criando uma terceira 
abstração que pega as informações como entrada e as passa para os outros. É basicamente para isso que uma API também 
é usada. """

# https://miro.medium.com/max/633/1*7rFi864XfIo2VGG9DCCF8g.png

"""
O conceito de design interessante desse princípio é que ele é a abordagem reversa do que normalmente faríamos.

Com o DIP em mente, começaríamos pelo final do projeto, no qual nosso código é independente do que recebe a entrada e 
não é suscetível a mudanças e está fora de nosso controle direto. Espero que você encontre esses conceitos úteis em 
sua codificação, eu sei que eles são para mim. Para saber mais, deixei alguns dos materiais que usei para entender 
esses princípios. 

"""