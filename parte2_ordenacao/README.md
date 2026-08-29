
## Algoritmo que Realizou Menos Operações para 10 Elementos

O Quick Sort realizou menos operações. No Bubble Sort foram realizadas 45 comparações e 26 trocas. Já no Quick Sort foram realizadas 23 comparações e 23 movimentações.

```python
# Execução do teste para 10 elementos
tamanho = 10
original = [random.randint(1, 1000) for _ in range(tamanho)]

lista_bubble = original.copy()
lista_quick = original.copy()

comparacoes_bubble, trocas_bubble = bubble_sort(lista_bubble)

comparacoes_quick = 0
movimentacoes_quick = 0
quicksort(lista_quick)

print("Tamanho:", tamanho)
print("Bubble - Comparações:", comparacoes_bubble)
print("Bubble - Trocas:", trocas_bubble)
print("Quick - Comparações:", comparacoes_quick)
print("Quick - Movimentações:", movimentacoes_quick)

```

## Comportamento para 20 Elementos

Com 20 elementos, o Quick Sort continuou realizando menos operações. O Bubble Sort realizou 190 comparações e 95 trocas, enquanto o Quick Sort realizou 63 comparações e 63 movimentações.

```python
# Execução do teste para 20 elementos
tamanho = 20
original = [random.randint(1, 1000) for _ in range(tamanho)]

lista_bubble = original.copy()
lista_quick = original.copy()

comparacoes_bubble, trocas_bubble = bubble_sort(lista_bubble)

comparacoes_quick = 0
movimentacoes_quick = 0
quicksort(lista_quick)

print("Tamanho:", tamanho)
print("Bubble - Comparações:", comparacoes_bubble)
print("Bubble - Trocas:", trocas_bubble)
print("Quick - Comparações:", comparacoes_quick)
print("Quick - Movimentações:", movimentacoes_quick)

```

## Impacto do Aumento para 1.000 Elementos

Quando o tamanho aumentou para 1.000 elementos, a diferença entre os algoritmos ficou muito maior. O Bubble Sort realizou 499.500 comparações e 243.427 trocas. Já no Quick Sort realizou 10.299 comparações e 10.299 movimentações.

```python
# Execução do teste para 1.000 elementos
tamanho = 1000
original = [random.randint(1, 1000) for _ in range(tamanho)]

lista_bubble = original.copy()
lista_quick = original.copy()

comparacoes_bubble, trocas_bubble = bubble_sort(lista_bubble)

comparacoes_quick = 0
movimentacoes_quick = 0
quicksort(lista_quick)

print("Tamanho:", tamanho)
print("Bubble - Comparações:", comparacoes_bubble)
print("Bubble - Trocas:", trocas_bubble)
print("Quick - Comparações:", comparacoes_quick)
print("Quick - Movimentações:", movimentacoes_quick)

```

## Algoritmo com Maior Crescimento na Quantidade de Operações

O Bubble Sort apresentou o maior crescimento. Isso acontece porque sua complexidade no caso médio é O(n²), fazendo com que a quantidade de operações aumente bastante conforme o tamanho da lista cresce.

```python
# Trecho do código que demonstra a estrutura de complexidade O(n²) do Bubble Sort
for i in range(len(lista)):
    for j in range(len(lista) - 1 - i):
        comparacoes += 1
        if lista[j] > lista[j + 1]:
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux
            trocas += 1

```

## Coerência entre Resultados Experimentais e Complexidades Teóricas

Os resultados experimentais são coerentes com as complexidades teóricas estudadas. O Bubble Sort possui complexidade média O(n²), enquanto o Quick Sort possui complexidade média O(n log n).

Os testes mostram exatamente esse comportamento: quando o número de elementos aumenta, o Bubble Sort cresce muito mais rapidamente que o Quick Sort.

```python
# Loop de automação dos testes para os diferentes tamanhos
for tamanho in [10, 20, 1000]:
    original = []

    for i in range(tamanho):
        original.append(random.randint(1, 1000))

    lista_bubble = original.copy()
    lista_quick = original.copy()

    comparacoes_bubble, trocas_bubble = bubble_sort(lista_bubble)

    comparacoes_quick = 0
    movimentacoes_quick = 0

    quicksort(lista_quick)

    print("\nTamanho:", tamanho)
    print("Bubble - Comparações:", comparacoes_bubble)
    print("Bubble - Trocas:", trocas_bubble)
    print("Quick - Comparações:", comparacoes_quick)
    print("Quick - Movimentações:", movimentacoes_quick)

```

## Situações para Escolha do Bubble Sort

Escolheríamos o Bubble Sort para listas pequenas ou situações em que a simplicidade do código seja mais importante que o desempenho.

```python
# Exemplo de chamada simples do Bubble Sort para um conjunto pequeno de dados
lista_pequena = [5, 2, 8, 1, 9]
comparacoes, trocas = bubble_sort(lista_pequena)
print("Lista pequena ordenada via Bubble Sort:", lista_pequena)

```

## Situações para Escolha do Quick Sort

Escolheríamos o Quick Sort para listas maiores, principalmente quando a eficiência da ordenação for importante. Como ele normalmente realiza menos operações que o Bubble Sort, é mais indicado para grandes quantidades de dados.

```python
# Exemplo de chamada do Quick Sort para uma lista com maior volume de dados
lista_grande = [random.randint(1, 1000) for _ in range(5000)]

comparacoes_quick = 0
movimentacoes_quick = 0

lista_ordenada = quicksort(lista_grande)
print("Quantidade de comparações para lista grande no Quick Sort:", comparacoes_quick)

```
### Tabela Comparativa de Desempenho e Complexidade

| Métria / Cenário | Bubble Sort | Quick Sort |
| :--- | :--- | :--- |
| **10 Elementos (Comparações)** | 45 | 23 |
| **10 Elementos (Trocas/Movimentações)** | 26 | 23 |
| **20 Elementos (Comparações)** | 190 | 63 |
| **20 Elementos (Trocas/Movimentações)** | 95 | 63 |
| **1.000 Elementos (Comparações)** | 499.500 | 10.299 |
| **1.000 Elementos (Trocas/Movimentações)** | 243.427 | 10.299 |
| **Complexidade Média (Teórica)** | $O(n^2)$ | $O(n \log n)$ |
| **Crescimento de Operações** | Muito mais rápido (Exponencial) | Moderado (Logarítmico) |
| **Melhor Indicação de Uso** | Listas pequenas / Simplicidade | Listas grandes / Desempenho |
