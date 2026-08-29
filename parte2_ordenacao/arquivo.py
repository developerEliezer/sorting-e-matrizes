import random

# BUBBLE SORT
# Recebe uma lista e ordena comparando elementos vizinhos.
# Também conta quantas comparações e trocas foram realizadas.
def bubble_sort(lista):
    comparacoes = 0
    trocas = 0

    # Percorre a lista várias vezes
    for i in range(len(lista)):

        # Compara os elementos vizinhos
        for j in range(len(lista) - 1 - i):
            comparacoes += 1

            # Se o elemento atual for maior que o próximo, realiza a troca
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

                trocas += 1

    # Retorna a quantidade de operações realizadas
    return comparacoes, trocas
    
# QUICK SORT
# Contadores das operações realizadas pelo Quick Sort
comparacoes_quick = 0
movimentacoes_quick = 0

# Ordena a lista utilizando um pivô para separar
# os elementos menores e maiores
def quicksort(lista):
    global comparacoes_quick, movimentacoes_quick

    # Se a lista tiver 0 ou 1 elemento, ela já está ordenada
    if len(lista) <= 1:
        return lista

    # O primeiro elemento da lista será usado como pivô
    pivo = lista[0]

    menores = []
    maiores = []

    # Percorre os elementos depois do pivô
    for x in lista[1:]:
        comparacoes_quick += 1

        # Se for menor ou igual ao pivô, vai para a lista de menores
        if x <= pivo:
            menores.append(x)

        # Se for maior que o pivô, vai para a lista de maiores
        else:
            maiores.append(x)

        # Conta cada elemento colocado em uma nova lista
        # como uma movimentação
        movimentacoes_quick += 1

    # Ordena novamente as partes menores e maiores
    return quicksort(menores) + [pivo] + quicksort(maiores)

# TESTES COM 10, 20 E 1000 ELEMENTOS
for tamanho in [10, 20, 1000]:

    original = []

    # Gera uma lista com números aleatórios
    for i in range(tamanho):
        original.append(random.randint(1, 1000))

    # Cria duas cópias para garantir que os dois algoritmos
    # utilizem exatamente os mesmos dados
    lista_bubble = original.copy()
    lista_quick = original.copy()

    # Executa o Bubble Sort e guarda suas operações
    comparacoes_bubble, trocas_bubble = bubble_sort(lista_bubble)

    # Zera os contadores antes de cada teste do Quick Sort
    comparacoes_quick = 0
    movimentacoes_quick = 0

    # Executa o Quick Sort
    quicksort(lista_quick)

    # Mostra os resultados de cada tamanho testado
    print("\nTamanho:", tamanho)

    print("Bubble - Comparações:", comparacoes_bubble)
    print("Bubble - Trocas:", trocas_bubble)

    print("Quick - Comparações:", comparacoes_quick)
    print("Quick - Movimentações:", movimentacoes_quick)
