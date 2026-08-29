<div align="justify">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O Quick Sort realizou menos operações. No Bubble Sort foram realizadas 45 comparações e 26 trocas. Já no Quick Sort foram realizadas 23 comparações e 23 movimentações.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Com 20 elementos, o Quick Sort continuou realizando menos operações. O Bubble Sort realizou 190 comparações e 95 trocas, enquanto o Quick Sort realizou 63 comparações e 63 movimentações.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quando o tamanho aumentou para 1.000 elementos, a diferença entre os algoritmos ficou muito maior. O Bubble Sort realizou 499.500 comparações e 243.427 trocas. Já no Quick Sort realizou 10.299 comparações e 10.299 movimentações.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O Bubble Sort apresentou o maior crescimento. Isso acontece porque sua complexidade no caso médio é O(n²), fazendo com que a quantidade de operações aumente bastante conforme o tamanho da lista cresce. Os resultados experimentais são coerentes com as complexidades teóricas estudadas. O Bubble Sort possui complexidade média O(n²), enquanto o Quick Sort possui complexidade média O(n log n).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Os tstes mostram exatamente esse comportamento: quando o número de elementos aumenta, o Bubble Sort cresce muito mais rapidamente que o Quick Sort.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Escolheríamos o Bubble Sort para listas pequenas ou situações em que a simplicidade do código seja mais importante que o desempenho.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Escolheríamos o Quick Sort para listas maiores, principalmente quando a eficiência da ordenação for importante. Como ele normalmente realiza menos operações que o Bubble Sort, é mais indicado para grandes quantidades de dados.

</div>
