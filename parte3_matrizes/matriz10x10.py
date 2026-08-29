# Busca na martrizs de 10x10
matriz = []

numero = 1

for i in range(10):
    linha = []

    for j in range(10):
        linha.append(numero)
        numero += 1

    matriz.append(linha)


valor = int(input("Digite o valor que deseja procurar: "))

comparacoes = 0
encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):

        comparacoes += 1

        if matriz[i][j] == valor:
            encontrado = True
            linha = i
            coluna = j
            break

    if encontrado:
        break

if encontrado:
    print("Valor encontrado!")
    print("Linha:", linha)
    print("Coluna:", coluna)
else:
    print("Valor não encontrado.")

print("Quantidade de comparações:", comparacoes)
