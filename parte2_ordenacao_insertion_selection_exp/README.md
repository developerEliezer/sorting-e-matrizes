# Análise Comparativa de Algoritmos de Ordenação em Python

Este projeto realiza uma análise experimental do desempenho e comportamento de quatro algoritmos clássicos de ordenação: **Bubble Sort**, **Insertion Sort**, **Selection Sort** e **Quick Sort**.

O objetivo é contabilizar e comparar o número de **comparações** e **movimentações/trocas** de elementos em diferentes cenários de entrada.

---

## Algoritmos Implementados

* **Bubble Sort**: Ordenação por comparação de elementos adjacentes.
* **Insertion Sort**: Ordenação por inserção direta elemento a elemento.
* **Selection Sort**: Ordenação por seleção do menor elemento a cada iteração.
* **Quick Sort**: Algoritmo de divisão e conquista baseado em particionamento (com pivô no final).

---

## Resultados dos Experimentos

Os dados abaixo foram gerados a partir da execução do código utilizando a semente fixa `random.seed(42)`.

### 1. Variação do Tamanho da Entrada (Vetores Aleatórios)

| Algoritmo | Tamanho (N) | Comparações | Trocas / Movimentações |
| :--- | :---: | :---: | :---: |
| **Bubble Sort** | 10 | 45 | 22 |
| **Insertion Sort** | 10 | 28 | 20 |
| **Selection Sort** | 10 | 45 | 8 |
| **Quick Sort** | 10 | 21 | 11 |
| | | | |
| **Bubble Sort** | 20 | 190 | 104 |
| **Insertion Sort** | 20 | 113 | 95 |
| **Selection Sort** | 20 | 190 | 16 |
| **Quick Sort** | 20 | 72 | 44 |
| | | | |
| **Bubble Sort** | 1000 | 499.500 | 253.250 |
| **Insertion Sort** | 1000 | 254.249 | 253.250 |
| **Selection Sort** | 1000 | 499.500 | 998 |
| **Quick Sort** | 1000 | 10.428 | 5.867 |

---

### 2. Análise de Cenários de Entrada (N = 100)

#### Vetor Aleatório (Caso Médio)
* **Bubble Sort**: Comparações = 4.950 | Trocas = 2.441
* **Insertion Sort**: Comparações = 2.540 | Movimentações = 2.441
* **Selection Sort**: Comparações = 4.950 | Trocas = 97
* **Quick Sort**: Comparações = 650 | Movimentações = 328

#### Vetor Já Ordenado (Melhor Caso)
* **Bubble Sort**: Comparações = 4.950 | Trocas = 0
* **Insertion Sort**: Comparações = 99 | Movimentações = 0
* **Selection Sort**: Comparações = 4.950 | Trocas = 0
* **Quick Sort**: Comparações = 4.950 | Movimentações = 0 *(Comportamento quadrático devido ao pivô fixo no final)*

#### Vetor Em Ordem Inversa (Pior Caso)
* **Bubble Sort**: Comparações = 4.950 | Trocas = 4.950
* **Insertion Sort**: Comparações = 4.950 | Movimentações = 4.950
* **Selection Sort**: Comparações = 4.950 | Trocas = 50
* **Quick Sort**: Comparações = 4.950 | Movimentações = 2.500

---

## Como Executar

**Requisito:** Python 3.x instalado.

Execute o script direto pelo terminal:

```bash
python main.py
```
