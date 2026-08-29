# PARTE 1 - PESQUISA: BUBBLE SORT E QUICK SORT

## 1. Algoritmo Bubble Sort

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Se trata de um algoritmo simples que ao receber uma lista percorre a estrutura de dados iterativamente, comparando elementos adjacentes em pares (<code>[j]</code> e <code>[j+1]</code>), se o elemento da esquerda for maior que o da direita a troca é realizada. O processo se repete em várias varreduras até que não precise fazer mais trocas. Os elementos com maior valor são movidos para o final da estrutura de forma gradual, por isso o nome deste tipo de algoritmo é Bubble Sort, é semelhante a bolhas de ar subindo na água. Esse processo é feito com dois laços de repetição (loops) aninhados, onde o loop externo funciona como um ponteiro de controle (índice <code>i</code>) que conta as passadas e delimita até onde comparar, empurrando o maior valor de cada varredura para a posição final, enquanto o loop interno gerencia o ponteiro móvel (índice <code>j</code>) que percorre a lista da esquerda para a direita fazendo as comparações e trocas entre os elementos vizinhos.
</p>

```python
def bubble_sort(lista):
    n = len(lista)
    
    # loop externo: ponteiro de controle (índice i) que conta as passadas e delimita até onde comparar
    for i in range(n - 1):
        trocou = False
        
        # loop interno: ponteiro móvel (índice j) que percorre a lista comparando elementos adjacentes em pares ([j] e [j+1])
        for j in range(n - 1 - i):
            # se o elemento da esquerda for maior que o da direita a troca é realizada
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        
        # se não precisar fazer mais trocas o processo encerra
        if not trocou:
            break
            
    return lista


# execução do código
minha_lista = [5, 2, 9, 1, 5, 6]
print(bubble_sort(minha_lista))
```

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No que tange à complexidade computacional do Bubble Sort, o melhor caso (<code>O(n)</code>) ocorre quando a lista já está ordenada, a implementação é otimizada com um algoritmo que faz apenas uma varredura com <code>n - 1</code> comparações e termina ao notar que não teve nenhuma troca. O caso médio (<code>O(n²)</code>) ocorre quando os elementos estão em ordem aleatória, o número de comparações é o mesmo do pior caso, mas aproximadamente metade delas resulta em troca. Já o pior caso (<code>O(n²)</code>) ocorre quando o array está em ordem inversa, fazendo todas as passadas possíveis; nessa condição, a soma das comparações em cada passada segue a sequência <code>(n-1) + (n-2) + ... + 1</code>, que resulta na fórmula <code>n(n-1)/2</code> e confirma matematicamente o comportamento quadrático.
</p>

| Caso | Complexidade | Justificativa Teórica e Matemática |
| --- | --- | --- |
| **Melhor Caso** | `O(n)` | A lista já está ordenada, o algoritmo faz apenas uma varredura com `n - 1` comparações e encerra sem fazer nenhuma troca usando a flag de controle |
| **Caso Médio** | `O(n²)` | Os elementos estão em ordem aleatória, realizando `n(n-1)/2` comparações onde aproximadamente metade resulta em trocas |
| **Pior Caso** | `O(n²)` | O array está em ordem inversa, o algoritmo faz todas as passadas possíveis somando `(n-1) + (n-2) + ... + 1`, gerando a fórmula `n(n-1)/2` comparações e trocas |

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Em relação às suas vantagens, o Bubble Sort é simples de entender e implementar, não precisa de memória extra para funcionar pois opera <i>in-place</i>, possui boa estabilidade ao preservar a ordem original de elementos iguais e apresenta excelente desempenho em listas pequenas ou dados quase ordenados com a otimização por flag. Como limitações, ele é altamente ineficiente para grandes volumes de dados devido ao crescimento quadrático do número de operações. Suas situações de uso adequado englobam listas muito pequenas, dados que já estão quase ordenados ou para fins didáticos. Por outro lado, suas situações não recomendadas incluem aplicações de alto desempenho, sistemas em tempo real, listas grandes, dados que mudam constantemente e listas desordenadas.
</p>

---

## 2. Algoritmo Quick Sort

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O Quick Sort é um algoritmo de ordenação eficiente que se baseia no padrão de projeto Divisão e Conquista, essa estratégia consiste em quebrar um problema em subproblemas menores, resolver eles individualmente e combinar os resultados no final. A fase de divisão ocorre no particionamento da estrutura, onde um elemento é escolhido como pivô e a lista é reorganizada de modo que todos os valores menores fiquem à sua esquerda e os maiores ou iguais à sua direita, posicionando o pivô em seu local definitivo. Esse processo é feito através de recursão — que é quando a função chama a si mesma durante a execução —, sendo invocada para a sublista da esquerda e da direita até atingir o caso base quando a sublista possui tamanho zero ou um elemento e a estrutura já se encontra ordenada. A eficiência e o desempenho dependem da escolha do pivô, podendo ser o primeiro elemento (<code>lista[0]</code>), o último (<code>lista[-1]</code>), o central (<code>lista[len(lista) // 2]</code>) ou a mediana de três que compara o primeiro, o central e o último elemento escolhendo o valor intermediário para evitar divisões desbalanceadas. Analisando a complexidade computacional, o melhor caso (<code>O(n log n)</code>) ocorre quando o pivô divide o array em metades aproximadamente iguais. O caso médio (<code>O(n log n)</code>) ocorre com elementos em ordem aleatória e divisões equilibradas na maioria das chamadas. Já o pior caso (<code>O(n²)</code>) ocorre quando o pivô escolhido é constantemente o maior ou o menor elemento, resultando em chamadas totalmente desbalanceadas.
</p>

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Analisando a implementação dos algoritmos sob a perspectiva do paradigma de Programação Orientada a Objetos (POO), o Bubble Sort e o Quick Sort refletem abordagens estruturais distintas no gerenciamento e na manipulação dos estados dos objetos. Em linguagens de alto nível e fortemente tipadas — como o Java —, o encapsulamento dessas rotinas em classes utilitárias ou métodos estáticos exige atenção redobrada ao comportamento das variáveis de referência durante as chamadas de métodos. Enquanto a ordenação <i>in-place</i> altera diretamente os atributos do objeto da lista original na memória heap, a criação de sublistas temporárias aloca novas referências na memória, demandando maior atuação do mecanismo de coleta de lixo (<i>Garbage Collector</i>) para limpar a memória restante de objetos que foram descartados durante a execução do programa.
</p>

```python
def quick_sort(lista):
    # caso base: sublistas de tamanho zero ou um já estão ordenadas
    if len(lista) <= 1:
        return lista
    
    # escolha do pivô usando o elemento central
    pivo = lista[len(lista) // 2]
    
    # particionamento da estrutura com base no pivô escolhido
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    
    # chamadas recursivas para as sublistas da esquerda e da direita concatenando os resultados
    return quick_sort(esquerda) + meio + quick_sort(direita)


# execução do código
minha_lista = [5, 2, 9, 1, 5, 6]
print(quick_sort(minha_lista))
```

| Caso | Complexidade | Justificativa Teórica e Matemática |
| --- | --- | --- |
| **Melhor Caso** | `O(n log n)` | O pivô divide a lista em duas metades iguais, criando uma árvore de recursão balanceada de altura `log₂(n)` com trabalho `O(n)` por nível. |
| **Caso Médio** | `O(n log n)` | Os elementos ficam em ordem aleatória e geram divisões equilibradas na maioria das chamadas recursivas. |
| **Pior Caso** | `O(n²)` | O pivô escolhido é constantemente o maior ou o menor elemento, gerando uma árvore totalmente desbalanceada com altura `n` e somatório de passadas. |

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dentre suas vantagens, o Quick Sort é extremamente rápido na prática para grandes volumes de dados e opera <i>in-place</i>, precisando de pouca memória extra (apenas a pilha de recursão), além de apresentar um excelente aproveitamento de cache de memória. Suas limitações residem no fato de não ser um algoritmo estável, podendo alterar a ordem de elementos iguais, e ter o risco do pior caso quadrático se o pivô não for bem escolhido. As situações de uso adequado referem-se a estruturas de dados de médio e grande porte, listas desordenadas, sistemas de alta performance e cenários onde o consumo de memória precisa ser baixo. Já as situações não recomendadas envolvem a necessidade de manter a ordem original de itens iguais, como ao reordenar uma lista sem estragar a ordenação de um filtro anterior. Também não é indicado quando o sistema exige um tempo de resposta rígido e sem margem para atrasos — já que um pivô mal escolhido pode deixar o processo lento —, nem para listas muito pequenas, onde gerenciar a recursão acaba dando mais trabalho do que usar um algoritmo mais simples.
</p>

<p align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A escolha da estrutura de dados subjacente também exerce um impacto direto no desempenho dessas rotinas de ordenação. Quando aplicamos o Quick Sort sobre um vetor estático ou uma lista encadeada, a eficiência do acesso indexado varia substancialmente: o acesso randômico direto por ponteiros de índice (como <code>[j]</code> ou <code>lista[i]</code>) possui complexidade constante <code>O(1)</code> em vetores contíguos na memória, enquanto em listas encadeadas a navegação até um elemento exige o percorrimento sequencial dos nós até o destino, elevando a complexidade de acesso. Dessa forma, a análise de complexidade temporal e espacial deve sempre considerar não apenas o algoritmo em si, mas a sinergia entre o código-fonte desenvolvido e os padrões de estruturas de dados utilizados no projeto.
</p>

---

### Análise Comparativa de Algoritmos de Ordenação: Bubble Sort e Quick Sort 

| Característica | Bubble Sort | Quick Sort |
| --- | --- | --- |
| **Princípio de funcionamento** | Varre a lista comparando e trocando elementos vizinhos em pares. | Aplica divisão e conquista, dividindo a lista a partir de um pivô com chamadas recursivas. |
| **Melhor caso** | `O(n)` | `O(n log n)` |
| **Caso médio** | `O(n²)` | `O(n log n)` |
| **Pior caso** | `O(n²)` | `O(n²)` |
| **Uso de memória** | `O(1)` (In-place pura, sem alocação extra). | `O(log n)` (In-place, necessitando apenas da pilha de recursão). |
| **Estabilidade** | Estável (preserva a ordem original de elementos com valores iguais). | Não estável (pode alterar a ordem relativa de elementos iguais). |
| **Vantagens principais** | Simples de entender e implementar; excelente em listas pequenas ou quase ordenadas. | Extremamente rápido na prática para grandes dados e ótimo aproveitamento de cache. |
| **Limitações principais** | Ineficiência severa para grandes volumes devido ao crescimento quadrático de operações. | Não preserva a ordem de itens iguais e corre risco de pior caso `O(n²)` se o pivô for ruim. |
| **Aplicações recomendadas** | Listas muito pequenas, dados quase ordenados ou fins didáticos. | Estruturas de médio e grande porte, listas desordenadas e sistemas de alta performance. |
| **Situações não recomendadas** | Aplicações de alto desempenho, listas grandes e dados que mudam constantemente. | Cenários que exigem estabilidade de dados, sistemas com tempo de resposta rígido ou listas pequenas. |
