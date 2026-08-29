# 🌡️ Parte 5 — Monitoramento de Sensores

> **Hands On 2 — Matriz Aplicada**

Nesta etapa da atividade foi desenvolvido um programa para representar o **monitoramento de temperaturas de 5 sensores ao longo de 24 horas**. Para armazenar essas informações, foi utilizada uma matriz com **5 linhas e 24 colunas**, totalizando **120 medições**.

Cada linha da matriz representa um sensor diferente, enquanto cada coluna representa um horário do dia, indo de **0 até 23 horas**.

---

## 📊 Funcionamento do programa

O programa percorre as temperaturas armazenadas na matriz e calcula a **média das 24 medições de cada sensor**. Em seguida, percorre os valores para encontrar a **maior temperatura registrada**, identificando também qual sensor realizou essa medição e em qual horário ela ocorreu.

Também é calculada a **média geral das 120 temperaturas** registradas pelos cinco sensores. Por fim, o programa verifica quantas medições ficaram acima de um determinado limite de temperatura.

---

## 🔁 Percorrendo a matriz

Para percorrer a matriz são necessários **loops aninhados**, pois os dados estão organizados em linhas e colunas. O primeiro `for` percorre as linhas, representando cada um dos 5 sensores, enquanto o segundo `for` percorre as 24 colunas, correspondentes aos horários.

Um exemplo utilizado no programa é:

```python
for i in range(5):
    for j in range(24):
        sensores[i][j]
```

Dessa maneira, para cada sensor são verificadas todas as suas 24 medições.

---

## 🔢 Índices `[i][j]`

Os índices `[i][j]` indicam qual posição da matriz está sendo acessada. Na expressão `sensores[i][j]`, o índice `i` representa a **linha da matriz (sensor)** e o índice `j` representa a **coluna (horário)**.

Por exemplo, `sensores[2][10]` representa o valor armazenado na linha de índice 2 e na coluna de índice 10. No programa, os sensores são apresentados na saída como sensores de **1 a 5**, enquanto os horários correspondem aos valores de **0 a 23**.

---

## 📐 Quantidade de posições e operações

A matriz utilizada possui **5 linhas × 24 colunas**, portanto existem:

**5 × 24 = 120 posições**

Sempre que a matriz é percorrida completamente, os loops passam pelas **120 posições**.

Isso demonstra a relação entre o número de linhas, o número de colunas e a quantidade de operações realizadas. De maneira geral, para uma matriz com `m` linhas e `n` colunas, um percurso completo precisa acessar `m × n` posições.

Por esse motivo, a complexidade de um percurso completo pela matriz pode ser representada como:

**O(m × n)**

Assim, conforme o número de linhas ou colunas aumenta, também aumenta a quantidade de posições que precisam ser percorridas pelo programa.

---

## 🤖 Observação sobre o desenvolvimento

Durante o desenvolvimento desta parte da atividade, tive dificuldade em **interpretar exatamente o que estava sendo solicitado no enunciado**. Por esse motivo, utilizei o **ChatGPT como ferramenta de apoio** para compreender melhor os requisitos apresentados e como eles poderiam ser organizados no código.

Após esse auxílio, analisei a solução desenvolvida e o funcionamento de cada parte do programa para compreender a implementação e os conceitos utilizados.
