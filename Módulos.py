
import math

numero = int(input("digite o número: "))
print("a raiz quadrada do número é: ", math.sqrt (numero))

import random

numero_aleatorio = random.randint(1,50)
print(numero_aleatorio)

import string

minha_string = input("digite a string: ")
contem_apenas_digitos = True
for caractere in minha_string:
    if caractere not in string.digits:
        contem_apenas_digitos = False
        break
if contem_apenas_digitos:
    print("A string contém apenas dígitos.")
else:
    print("A string não contém apenas dígitos.")