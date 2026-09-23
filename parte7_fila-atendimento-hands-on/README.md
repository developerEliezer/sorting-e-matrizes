# Sistema Inteligente de Atendimento

Este projeto tem como objetivo desenvolver um sistema de atendimento utilizando diferentes estruturas de fila em Python. O sistema simula uma central de atendimento onde cada cliente possui um nome, uma senha e uma prioridade, que pode ser 1 para emergência, 2 para atendimento prioritário ou 3 para atendimento normal.

Durante o desenvolvimento foram implementadas três formas diferentes de organização dos clientes. A primeira foi a fila clássica, baseada no conceito FIFO (First In, First Out), onde o primeiro cliente a entrar é o primeiro a ser atendido. Também foi desenvolvida uma fila circular com capacidade para cinco clientes, permitindo que as posições liberadas sejam reutilizadas durante o atendimento. Por fim, foi implementada uma fila de prioridade utilizando a biblioteca `heapq`, fazendo com que os clientes de maior prioridade de atendimento sejam atendidos primeiro. Quando dois clientes possuem a mesma prioridade, a ordem de chegada é mantida.

Além das implementações individuais, foi desenvolvido um desafio final que gera automaticamente 20 clientes, atribuindo a cada um uma senha e uma prioridade aleatória entre 1 e 3. Esses clientes são utilizados nas três estruturas para demonstrar, na prática, as diferenças entre os métodos de organização e atendimento.

Com o desenvolvimento do projeto foi possível compreender melhor o funcionamento das filas, suas operações de inserção e remoção, o funcionamento da fila circular e o uso de prioridades para organizar atendimentos. Também foi possível observar que cada estrutura possui uma forma diferente de organizar os elementos e pode ser utilizada de acordo com a necessidade do sistema.
