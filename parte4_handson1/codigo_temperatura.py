temperaturas = []

for i in range(10):
    temperatura = float(input("Digite a temperatura:"))
    temperaturas.append(temperatura) 
    
print("\nTemperaturas armazenadas:")

for i in range(len(temperaturas)):
    print("Índice:", i, "Temperatura:", temperaturas[i])
    
soma = 0

for i in range(len(temperaturas)):
    soma += temperaturas[i]
    
media = soma / len(temperaturas)

maior = temperaturas[0]
menor = temperaturas[0]
    
indice_maior = 0    
indice_menor = 0  

for i in range(len(temperaturas)):
    
    if temperaturas[i] > maior:
        maior = temperaturas[i]
        indice_maior = i

    if temperaturas[i] < menor:
        menor = temperaturas[i]
        indice_menor = i

acima_media = 0

for i in range(len(temperaturas)):
    
    if temperaturas[i] > media:
        acima_media += 1

print("\n----- RESULTADOS -----")

print("Média:", media)
print("Maior temperatura:", maior)
print("Índice do maior:", indice_maior)
print("Menor temperatura:", menor)
print("Índice do menor:", indice_menor)
print("Temperaturas acima da média:", acima_media)

#Terminal
Temperaturas armazenadas:
Índice: 0 Temperatura: 20.0
Índice: 1 Temperatura: 22.0
Índice: 2 Temperatura: 18.0
Índice: 3 Temperatura: 25.0
Índice: 4 Temperatura: 30.0
Índice: 5 Temperatura: 21.0
Índice: 6 Temperatura: 19.0
Índice: 7 Temperatura: 27.0
Índice: 8 Temperatura: 23.0
Índice: 9 Temperatura: 24.0

----- RESULTADOS -----
Média: 22.9
Maior temperatura: 30.0
Índice do maior: 4
Menor temperatura: 18.0
Índice do menor: 2
Temperaturas acima da média: 5
