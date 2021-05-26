"""
from random import choice


gen = (str(x) for x in range(1, 10000))
print(choice(tuple(gen)))

"""
import pywhatkit

prefixo = "+55319"
numero = input(str())

numero_completo = prefixo + numero
print(numero_completo)
mensagem = str(input("Digite sua mensagem : "))
hora = int(input("Digite a hora : "))
minutos = int(input("Digite os minutos (apenas os minutos)"))

pywhatkit.sendwhatmsg(numero_completo,mensagem,hora,minutos)
