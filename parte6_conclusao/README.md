# 📊 PARTE 6 – ANÁLISE E CONCLUSÃO

---

## 📌 Análise Comparativa dos Experimentos

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O aumento no tamanho da estrutura de dados influencia diretamente a quantidade de operações executadas pelos algoritmos. Na busca sequencial em matrizes, a quantidade de comparações no pior caso cresce exatamente na mesma proporção do total de elementos (m × n): na matriz 2 × 2 foram 4 comparações, na 10 × 10 subiu para 100 e na 100 × 100 chegou a 10.000 comparações. O mesmo impacto ocorreu no experimento de ordenação, onde a expansão do array de 10 para 1.000 elementos disparou o volume de processamento em ambos os métodos.
</p>

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contudo, Bubble Sort e Quick Sort não crescem do mesmo jeito conforme o volume de dados aumenta. Devido à sua complexidade média de O(n²), o Bubble Sort opera em dois loops aninhados comparando pares adjacentes, o que faz o número de operações explodir: no teste com 10 elementos ele executou 45 comparações, mas com 1.000 elementos esse valor saltou para 499.500 comparações e 243.427 trocas. Por outro lado, o Quick Sort aplica Divisão e Conquista com recursão e pivô, mantendo uma complexidade média de O(n log n). Para ordenar os mesmos 1.000 elementos, ele precisou de apenas 10.299 comparações e 10.299 movimentações, provando ser significativamente mais eficiente em escalas maiores.
</p>

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Diante disso, analisar apenas o resultado final da ordenação não é suficiente para comparar algoritmos. Como ambos entregam o array perfeitamente ordenado no término da execução, limitar a avaliação ao estado final esconde todo o custo computacional, o tempo de resposta e o gargalo de processamento gerados durante o percurso. Para 1.000 itens, o Bubble Sort realizou cerca de 50 vezes mais comparações que o Quick Sort, o que em produção representa consumo excessivo de CPU e degradação de desempenho. Além disso, a análise do resultado omite fatores estruturais como o consumo de memória — nulo no Bubble Sort e existente na pilha de recursão do Quick Sort (O(log n)) — e a estabilidade do algoritmo.
</p>

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Por fim, vale destacar que ferramentas de inteligência artificial foram utilizadas no suporte a este projeto, servindo para auxiliar na formatação do texto, estrutura do repositório em Markdown e montagem das tabelas comparativas. O conteúdo teórico, a análise dos dados e a redação foram revisados, pesquisados e reescritos manualmente pelo grupo diversas vezes para garantir o alinhamento com os experimentos executados, utilizando a IA estritamente como um recurso de organização visual e produtividade.
</p>

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

### 2. Experimento de Busca Sequencial (Matrizes)

| Dimensão da Matriz | Nº Total de Elementos | Busca no Início | Busca no Final | Valor Inexistente | Complexidade |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **2 × 2** | 4 elementos | 1 comparação | 4 comparações | 4 comparações | O(m × n) |
| **10 × 10** | 100 elementos | 1 comparação | 100 comparações | 100 comparações | O(m × n) |
| **100 × 100** | 10.000 elementos | 1 comparação | 10.000 comparações | 10.000 comparações | O(m × n) |
