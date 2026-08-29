## Resultados da Busca em Matrizes

| **Matriz** | **Nº de elementos** | **Busca no início** | **Busca no final** | **Valor inexistente** |
|---|---:|---:|---:|---:|
| 2 × 2 | 4 | **1** | **4** | **4** |
| 10 × 10 | 100 | **1** | **100** | **100** |
| 100 × 100 | 10.000 | **1** | **10.000** | **10.000** |

## Perguntas

### a) Por que encontrar um elemento no início exige menos operações?

Porque a busca sequencial começa pela primeira posição da matriz. Se o valor procurado estiver no início, ele será encontrado logo na primeira comparação, sem precisar verificar os outros elementos.

### b) O que acontece quando o elemento procurado não existe?

O algoritmo precisa percorrer todas as posições da matriz para ter certeza de que o valor não está presente. Por isso, a quantidade de comparações será igual ao número total de elementos.

### c) Qual é o pior caso da busca sequencial?

O pior caso acontece quando o elemento procurado está na **última posição** ou quando o elemento **não existe** na matriz. Nessas situações, todos os elementos precisam ser comparados.

### d) Como o aumento das dimensões da matriz influencia a quantidade de operações?

Quanto maior a matriz, maior será a quantidade de elementos que podem precisar ser analisados.

Por exemplo:

| Matriz | Quantidade de elementos |
|---|---:|
| 2 × 2 | 4 elementos |
| 10 × 10 | 100 elementos |
| 100 × 100 | 10.000 elementos |

Assim, no pior caso, a quantidade de comparações aumenta de acordo com a quantidade de elementos da matriz.

### e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?

Uma matriz com `m` linhas e `n` colunas possui:

**m × n elementos**

No pior caso, a busca pode precisar verificar todos eles.

Portanto, a complexidade é:

**O(m × n)**

Se for uma matriz quadrada, como `n × n`, podemos representar como:

**O(n²)**
