# 1 Média de uma lista
numeros = [5,10,15,20,25]
soma = 0
for numero in numeros:
    soma+= numero
    
media = soma / len(numeros)
print("A média dos números é:", media)

# 2 Maior e menor
palavras = ["programação", "python", "variável", "print", "código"]
palavra_maior = palavras[0]
palavra_menor = palavras[0]

for palavra in palavras:
    if len(palavra) > len(palavra_maior):
        palavra_maior = palavra
    if len(palavra) < len(palavra_menor):
        palavra_menor = palavra

print("A maior palavra é:", palavra_maior)
print("A menor palavra é:", palavra_menor)

# 3 Detectando palavras
palavra = input("Digite a palavra: ")

palavra_invertida = palavra[::-1]
palindromo = palavra == palavra_invertida

if palindromo:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")

# 4 Utilizando índices
def indice_do_alfabeto(indice):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if 1 <= indice <= 26:
        return alfabeto[indice - 1]
    else:
        return None
    
print("O indice do alfabeto é a letra:", indice_do_alfabeto(1))    