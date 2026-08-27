# PARTE 1 - PESQUISA: BUBBLE SORT E QUICK SORT

## 1. Algoritmo Bubble Sort

- **Como funciona:** Se trata de um algoritmo simples que ao receber uma lista percorre a estrutura de dados iterativamente, comparando elementos adjacentes em pares ($[j]$ e $[j+1]$), se o elemento da esquerda for maior que o da direita a troca é realizada. O processo se repete em várias varreduras até que não precise fazer mais trocas.
- **Lógica de ordenação:** Os elementos com maior valor são movidos para o final da estrutura de forma gradual, por isso o nome deste tipo de algoritmo é Bubble Sort, é semelhante a bolhas de ar subindo na água.
- **Complexidade Computacional:**
  - **Melhor caso ($O(n)$):** ocorre quando a lista já está ordenada, sua implementação é otimizada com um algoritmo que faz apenas uma varredura e termina.
  - **Caso médio ($O(n^2)$):** ocorre quando os elementos estão em ordem aleatória. O número de comparações é o mesmo do pior caso, mas aproximadamente metade delas resulta em troca.
  - **Pior caso ($O(n^2)$):** ocorre quando o array está em ordem inversa. Cada comparação resulta em uma troca e o algoritmo só para depois de fazer todas as passadas possíveis.
- **Vantagens:** É simples de entender e implementar; ele não precisa de memória extra para funcionar; possui boa estabilidade (preserva a ordem de elementos iguais).
- **Limitações:** É altamente ineficiente para grandes volumes de dados pois há crescimento quadrático do número de operações.
- **Situações de uso adequado:** Listas muito pequenas, dados que já estão quase ordenados ou para fins didáticos.
- **Situações não recomendadas:** Aplicações de alto desempenho, sistemas em tempo real, listas grandes, dados que mudam constantemente e listas desordenadas.

---

## 2. Algoritmo Quick Sort

- **Como funciona:** É um algoritmo eficiente, sua metodologia é baseada na divisão e conquista. Ao receber uma lista, é escolhido um elemento para ser o pivô, dividimos a estrutura de dados de forma que os elementos menores que o pivô fiquem à esquerda e os maiores à direita. O processo se repete para as sublistas até que toda a estrutura esteja ordenada.
- **Lógica de ordenação:** Em vez de tentar organizar a lista inteira de uma vez, a estratégia foca em definir posições definitivas por etapas. Ao colocar todos os números menores de um lado e os maiores do outro, o algoritmo garante que o pivô já fique na sua posição final perfeita e os dois lados formados ficam isolados, eliminando a necessidade de comparar elementos do lado esquerdo com os do lado direito.
- **Complexidade Computacional:**
  - **Melhor caso ($O(n \log n)$):** ocorre quando o pivô divide o array sempre em metades aproximadamente iguais.
  - **Caso médio ($O(n \log n)$):** ocorre quando os elementos estão em ordem aleatória, escolha do pivô divide o array de forma equilibrada na maioria das chamadas.
  - **Pior caso ($O(n^2)$):** ocorre quando o pivô escolhido é sempre o maior ou menor elemento.
- **Vantagens:** É extremamente rápido na prática para grandes volumes de dados e opera *in-place*, utilizando pouca memória extra. Apresenta um excelente aproveitamento de cache de memória.
- **Limitações:** Pode alterar a ordem relativa de elementos iguais, portanto não é um algoritmo estável, possui um pior caso com desempenho quadrático se não escolher corretamente o pivô.
- **Situações de uso adequado:** Estruturas de dados de médio e grande porte, listas desordenadas, sistemas que exigem alta performance e cenários onde o consumo de memória precisa ser baixo.
- **Situações não recomendadas:** Manter a ordem original de itens com o mesmo valor, como ao reordenar uma lista sem bagunçar um filtro anterior. Também evitar quando o sistema exige um tempo de resposta cravado e sem margem para atrasos, já que um pivô mal escolhido pode deixar o processo lento, ou em listas muito pequenas, onde controlar toda a recursão dá mais trabalho do que simplesmente aplicar um método mais simples.

---

## Tabela Comparativa

| Característica | Bubble Sort | Quick Sort |
| :--- | :--- | :--- |
| **Princípio de funcionamento** | Comparação e troca de elementos vizinhos | Divisão e conquista com escolha de pivô e particionamento |
| **Melhor caso** | $O(n)$ | $O(n \log n)$ |
| **Caso médio** | $O(n^2)$ | $O(n \log n)$ |
| **Pior caso** | $O(n^2)$ | $O(n^2)$ |
| **Uso de memória** | $O(1)$ (In-place) | $O(\log n)$ (Pilha de recursão) |
| **Vantagem principal** | Simplicidade e baixo custo para dados quase ordenados | Altíssima eficiência e velocidade para grandes volumes de dados |
| **Limitação principal** | Ineficiência severa para grandes dados ($O(n^2)$) | Risco de $O(n^2)$ no pior caso dependendo da escolha do pivô |
| **Aplicação recomendada** | Listas pequenas ou dados quase ordenados | Ordenação geral de dados de médio e grande porte |