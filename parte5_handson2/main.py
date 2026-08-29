# PARTE 5 - MONITORAMENTO DE SENSORES

# Matriz que armazena as temperaturas.
# São 5 linhas, representando os 5 sensores.
# Cada linha possui 24 valores, representando as 24 horas do dia.
# Portanto, temos 5 x 24 = 120 medições.
sensores = [
    [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 19],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 20],
    [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20],
    [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21],
    [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]
]


# 1. MÉDIA DE CADA SENSOR

# O índice "i" representa o sensor.
# O primeiro for percorre os 5 sensores.
for i in range(5):

    # Começa a soma das temperaturas do sensor atual em zero.
    soma = 0

    # O índice "j" representa o horário.
    # Este for percorre as 24 horas do sensor atual.
    for j in range(24):
        soma += sensores[i][j]

    # Divide a soma das 24 temperaturas por 24.
    media = soma / 24

    # round(media, 2) mostra a média com duas casas decimais.
    # i + 1 faz os sensores aparecerem como 1, 2, 3, 4 e 5.
    print("Média do sensor", i + 1, ":", round(media, 2))


# 2, 3 E 4. MAIOR TEMPERATURA, SENSOR E HORÁRIO

# Considera inicialmente a primeira temperatura
# da matriz como sendo a maior.
maior = sensores[0][0]

# Variável que guarda o sensor da maior temperatura.
sensor = 0

# Variável que guarda o horário da maior temperatura.
horario = 0


# Percorre todas as linhas (sensores).
for i in range(5):

    # Percorre todas as colunas (horários).
    for j in range(24):

        # Verifica se a temperatura atual é maior
        # que a maior temperatura encontrada até agora.
        if sensores[i][j] > maior:

            # Atualiza a maior temperatura.
            maior = sensores[i][j]

            # Guarda o índice do sensor.
            sensor = i

            # Guarda o índice do horário.
            horario = j


# Mostra a maior temperatura encontrada.
print("\nMaior temperatura:", maior, "°C")

# Soma 1 porque queremos mostrar os sensores de 1 até 5.
print("Sensor:", sensor + 1)

# O índice da coluna já corresponde ao horário de 0 até 23.
print("Horário:", horario)


# 5. MÉDIA GERAL

# Começa uma nova soma em zero.
soma = 0

# Percorre novamente os 5 sensores.
for i in range(5):

    # Percorre as 24 medições de cada sensor.
    for j in range(24):

        # Soma todas as temperaturas da matriz.
        soma += sensores[i][j]


# Existem 5 sensores com 24 medições cada.
# 5 x 24 = 120 medições.
# Por isso, dividimos a soma total por 120.
media_geral = soma / 120

# Mostra a média geral com duas casas decimais.
print("Média geral:", round(media_geral, 2), "°C")


# 6. LEITURAS ACIMA DO LIMITE

# Limite utilizado no teste.
# Neste caso, queremos descobrir quantas temperaturas
# ficaram acima de 28 °C.
limite = 28

# Contador que começa em zero.
quantidade = 0


# Percorre toda a matriz.
for i in range(5):
    for j in range(24):

        # Verifica se a temperatura atual está acima do limite.
        if sensores[i][j] > limite:

            # Se estiver acima, aumenta o contador em 1.
            quantidade += 1


# Mostra o limite utilizado.
print("Limite informado:", limite, "°C")

# Mostra quantas medições ficaram acima do limite.
print("Leituras acima do limite:", quantidade)
