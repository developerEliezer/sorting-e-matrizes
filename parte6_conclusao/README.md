# 📊 PARTE 6 – ANÁLISE E CONCLUSÃO

> **Atividade Avaliativa – Estrutura de Dados II**  
> **Integrantes:** Pedro Henrique Farias da Silva, Eliezer Câmara Silva Filho, Welinton Junior

---

## 📌 Análise Comparativa dos Experimentos

<div align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O aumento no tamanho da estrutura de dados influencia diretamente a quantidade de operações executadas pelos algoritmos. Na busca sequencial em matrizes, a quantidade de comparações no pior caso cresce exatamente na mesma proporção do total de elementos (m × n): na matriz 2 × 2 foram 4 comparações, na 10 × 10 subiu para 100 e na 100 × 100 chegou a 10.000 comparações. O mesmo impacto ocorreu no experimento de ordenação, onde a expansão do array de 10 para 1.000 elementos disparou o volume de processamento em ambos os métodos.
</div>

<br>

<div align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Esse comportamento linear também fica evidente na manipulação de arrays unidimensionais, como demonstrado na análise do vetor de temperaturas. Ao percorrer a lista para calcular a média, identificar o maior e o menor valor com seus respectivos índices e contabilizar as temperaturas acima da média, o algoritmo executa iterações consecutivas sobre os dados. Com 10 elementos, são percorridas aproximadamente 50 posições somando as etapas do programa; com 1.000 elementos, esse volume escala proporcionalmente para cerca de 5.000 iterações. Por não haver loops aninhados nesse fluxo, a estrutura mantém uma complexidade linear O(n), servindo como contraponto direto aos métodos de ordenação mais custosos.
</div>

<br>

<div align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contudo, Bubble Sort e Quick Sort não crescem do mesmo jeito conforme o volume de dados aumenta. Devido à sua complexidade média de O(n²), o Bubble Sort opera em dois loops aninhados comparando pares adjacentes, o que faz o número de operações explodir: no teste com 10 elementos ele executou 45 comparações, mas com 1.000 elementos esse valor saltou para 499.500 comparações e 243.427 trocas. Por outro lado, o Quick Sort aplica Divisão e Conquista com recursão e pivô, mantendo uma complexidade média de O(n log n). Para ordenar os mesmos 1.000 elementos, ele precisou de apenas 10.299 comparações e 10.299 movimentações, provando ser significativamente mais eficiente em escalas maiores.
</div>

<br>

<div align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Diante disso, analisar apenas o resultado final da ordenação não é suficiente para comparar algoritmos. Como ambos entregam o array perfeitamente ordenado no término da execução, limitar a avaliação ao estado final esconde todo o custo computacional, o tempo de resposta e o gargalo de processamento gerados durante o percurso. Para 1.000 itens, o Bubble Sort realizou cerca de 50 vezes mais comparações que o Quick Sort, o que em produção representa consumo excessivo de CPU e degradação de desempenho. Além disso, a análise do resultado omite fatores estruturais como o consumo de memória — nulo no Bubble Sort e existente na pilha de recursão do Quick Sort (O(log n)) — e a estabilidade do algoritmo.
</div>

<br>

<div align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Por fim, vale destacar que ferramentas de inteligência artificial foram utilizadas no suporte a este projeto, servindo para auxiliar na formatação do texto, estrutura do repositório em Markdown e montagem das tabelas comparativas. O conteúdo teórico e a análise dos dados foram revisados, pesquisados e reescritos manualmente pelo grupo diversas vezes para garantir o alinhamento com os experimentos executados, utilizando a IA estritamente como um recurso de organização visual e produtividade.
</div>

---

## 📈 Resultados Experimentais

### 1. Experimento de Ordenação (Arrays)

| Tamanho da Lista | Algoritmo | Comparações | Trocas / Movimentações | Complexidade Teórica (Médio Caso) |
| :---: | :---: | :---: | :---: | :---: |
| **10 elementos** | **Bubble Sort** | 45 | 26 | O(n²) |
| | **Quick Sort** | 23 | 23 | O(n log n) |
| **20 elementos** | **Bubble Sort** | 190 | 95 | O(n²) |
| | **Quick Sort** | 63 | 63 | O(n log n) |
| **1.000 elementos** | **Bubble Sort** | 499.500 | 243.427 | O(n²) |
| | **Quick Sort** | 10.299 | 10.299 | O(n log n) |

---

### 2. Experimento de Análise Linear (Vetor de Temperaturas)

#### Dados do Experimento
| Índice | Temperatura (°C) | Condição em Relação à Média |
| :---: | :---: | :---: |
| **0** | 20.0 | Abaixo |
| **1** | 22.0 | Abaixo |
| **2** | 18.0 *(Menor)* | Abaixo |
| **3** | 25.0 | **Acima** |
| **4** | 30.0 *(Maior)* | **Acima** |
| **5** | 21.0 | Abaixo |
| **6** | 19.0 | Abaixo |
| **7** | 27.0 | **Acima** |
| **8** | 23.0 | **Acima** |
| **9** | 24.0 | **Acima** |

#### Métricas Processadas
| Métrica | Valor Obtido |
| :--- | :---: |
| **Média das Temperaturas** | 22.9 °C |
| **Maior Temperatura** | 30.0 °C (Índice 4) |
| **Menor Temperatura** | 18.0 °C (Índice 2) |
| **Temperaturas Acima da Média** | 5 |

#### Escala e Complexidade Algorítmica
| Elementos (n) | Posições Percorridas (Aprox.) | Complexidade Teórica |
| :---: | :---: | :---: |
| **10 temperaturas** | ~50 iterações | O(n) |
| **100 temperaturas** | ~500 iterações | O(n) |
| **1.000 temperaturas** | ~5.000 iterações | O(n) |

---

### 3. Experimento de Busca Sequencial (Matrizes)

| Dimensão da Matriz | Nº Total de Elementos | Busca no Início | Busca no Final | Valor Inexistente | Complexidade |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2 × 2** | 4 elementos | 1 comparação | 4 comparações | 4 comparações | O(m × n) |
| **10 × 10** | 100 elementos | 1 comparação | 100 comparações | 100 comparações | O(m × n) |
| **100 × 100** | 10.000 elementos | 1 comparação | 10.000 comparações | 10.000 comparações | O(m × n) |
