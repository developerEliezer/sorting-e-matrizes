# Sistema Inteligente de Atendimento

Este projeto tem como objetivo desenvolver um sistema de atendimento utilizando diferentes estruturas de fila em Python. O sistema simula uma central de atendimento onde cada cliente possui um nome, uma senha e uma prioridade, que pode ser 1 para emergência, 2 para atendimento prioritário ou 3 para atendimento normal.

Durante o desenvolvimento foram implementadas três formas diferentes de organização dos clientes. A primeira foi a fila clássica, baseada no conceito FIFO (First In, First Out), onde o primeiro cliente a entrar é o primeiro a ser atendido. Também foi desenvolvida uma fila circular com capacidade para cinco clientes, permitindo que as posições liberadas sejam reutilizadas durante o atendimento. Por fim, foi implementada uma fila de prioridade utilizando a biblioteca `heapq`, fazendo com que os clientes de maior prioridade de atendimento sejam atendidos primeiro. Quando dois clientes possuem a mesma prioridade, a ordem de chegada é mantida.

Além das implementações individuais, foi desenvolvido um desafio final que gera automaticamente 20 clientes, atribuindo a cada um uma senha e uma prioridade aleatória entre 1 e 3. Esses clientes são utilizados nas três estruturas para demonstrar, na prática, as diferenças entre os métodos de organização e atendimento.

Com o desenvolvimento do projeto foi possível compreender melhor o funcionamento das filas, suas operações de inserção e remoção, o funcionamento da fila circular e o uso de prioridades para organizar atendimentos. Também foi possível observar que cada estrutura possui uma forma diferente de organizar os elementos e pode ser utilizada de acordo com a necessidade do sistema.
# Sistema Inteligente de Atendimento

Este projeto tem como objetivo desenvolver um sistema de atendimento utilizando diferentes estruturas de fila em Python. O sistema simula uma central de atendimento onde cada cliente possui um nome, uma senha e uma prioridade, que pode ser 1 para emergência, 2 para atendimento prioritário ou 3 para atendimento normal.

Durante o desenvolvimento foram implementadas três formas diferentes de organização dos clientes. A primeira foi a fila clássica, baseada no conceito FIFO (First In, First Out), onde o primeiro cliente a entrar é o primeiro a ser atendido. Também foi desenvolvida uma fila circular com capacidade para cinco clientes, permitindo que as posições liberadas sejam reutilizadas durante o atendimento. Por fim, foi implementada uma fila de prioridade utilizando a biblioteca `heapq`, fazendo com que os clientes de maior prioridade de atendimento sejam atendidos primeiro. Quando dois clientes possuem a mesma prioridade, a ordem de chegada é mantida.

Além das implementações individuais, foi desenvolvido um desafio final que gera automaticamente 20 clientes, atribuindo a cada um uma senha e uma prioridade aleatória entre 1 e 3. Esses clientes são utilizados nas três estruturas para demonstrar, na prática, as diferenças entre os métodos de organização e atendimento.

Com o desenvolvimento do projeto foi possível compreender melhor o funcionamento das filas, suas operações de inserção e remoção, o funcionamento da fila circular e o uso de prioridades para organizar atendimentos. Também foi possível observar que cada estrutura possui uma forma diferente de organizar os elementos e pode ser utilizada de acordo com a necessidade do sistema.

---

## Perguntas e respostas

### Por que a ordem de atendimento da fila de prioridade pode ser diferente da ordem da fila clássica?

Na fila clássica, os clientes são atendidos seguindo a ordem de chegada, ou seja, quem entra primeiro é atendido primeiro. Já na fila de prioridade, o atendimento considera a prioridade de cada cliente. Dessa forma, um cliente que chegou depois pode ser atendido antes de outro que chegou primeiro se possuir uma prioridade maior. No sistema desenvolvido, a prioridade 1 representa uma emergência, então esse cliente será atendido antes dos clientes com prioridade 2 ou 3. Quando dois clientes possuem a mesma prioridade, a ordem de chegada é mantida.

### 1. Em quais situações reais uma fila de prioridade seria mais adequada?

A fila de prioridade é mais adequada em situações em que algumas pessoas ou tarefas precisam ser atendidas antes das outras. Um exemplo é um hospital, onde pacientes em situações mais graves podem precisar de atendimento antes de pacientes em situações menos urgentes. Também pode ser utilizada em serviços de emergência, sistemas de atendimento ao cliente, processamento de tarefas em computadores e outros sistemas onde é necessário definir uma ordem de importância.

### 2. Quais são as vantagens e limitações de uma fila circular?

Uma das principais vantagens da fila circular é a possibilidade de reutilizar as posições que ficam vazias depois que os elementos são removidos. Isso evita desperdício de espaço e é útil quando a fila possui uma capacidade fixa. No projeto, a fila circular possui espaço para cinco clientes e, quando alguns são atendidos, as posições liberadas podem ser utilizadas novamente.

Como limitação, é necessário controlar corretamente as posições de entrada e saída da fila para evitar erros. Além disso, quando a fila está completamente cheia, não é possível adicionar novos elementos até que algum cliente seja atendido e uma posição seja liberada.

### 3. O que acontece ao tentar inserir um elemento em uma fila circular cheia?

Quando uma fila circular está cheia, não existe espaço disponível para receber um novo elemento. No código desenvolvido, a inserção verifica se ainda existe espaço na fila antes de adicionar um novo cliente. Se a capacidade máxima já tiver sido atingida, o novo cliente não é inserido até que algum elemento seja removido.

---

## Conclusão

O desenvolvimento do Sistema Inteligente de Atendimento permitiu compreender, na prática, as diferenças entre uma fila clássica, uma fila circular e uma fila de prioridade. A fila clássica mantém a ordem de chegada, a fila circular permite reutilizar posições disponíveis e a fila de prioridade organiza o atendimento de acordo com a importância de cada cliente.

Com os testes realizados, foi possível perceber que não existe apenas uma forma de organizar uma fila. Cada estrutura pode ser utilizada de acordo com a necessidade do sistema. Dessa forma, o projeto ajudou a entender como as estruturas de dados podem ser aplicadas em situações próximas das que encontramos no dia a dia.
