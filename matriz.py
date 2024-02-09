linhas = 3
colunas = 3
tabela = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = int(input(f"Digite o número para a posição [{i+1}][{j+1}]: "))
        linha.append(numero)
    tabela.append(linha)
soma_linhas = []
for linha in tabela:
    soma_linha = sum(linha)
    soma_linhas.append(soma_linha)
soma_total = sum(sum(linha) for linha in tabela)
print("Soma de cada linha:")
for i in range(len(soma_linhas)):
    print("Linha", i + 1, ":", soma_linhas[i])
print("Soma de todos os elementos:", soma_total)

matriz = [[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]]
for l in range(0,3):
  for c in range(0,3):
    matriz [l] [c] = int(input(f"digite o valor para [{l}] [{c}]: "))
print("-=" * 30)
for l in range(0,3):
  for c in range(0,3):
      print(f"[{matriz [l] [c]:^5}]", end =" ")
  print()