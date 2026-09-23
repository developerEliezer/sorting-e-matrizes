import random
import heapq


# =========================
# FILA CLÁSSICA
# =========================

class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, cliente):
        self.fila.append(cliente)

    def dequeue(self):
        if self.fila:
            return self.fila.pop(0)

    def empty(self):
        return len(self.fila) == 0


# =========================
# FILA CIRCULAR
# =========================

class FilaCircular:
    def __init__(self):
        self.fila = [None] * 5
        self.front = 0
        self.rear = 0
        self.tamanho = 0

    def enqueue(self, cliente):
        if self.tamanho < 5:
            self.fila[self.rear] = cliente
            self.rear = (self.rear + 1) % 5
            self.tamanho += 1

    def dequeue(self):
        if self.tamanho > 0:
            cliente = self.fila[self.front]
            self.fila[self.front] = None
            self.front = (self.front + 1) % 5
            self.tamanho -= 1
            return cliente


# =========================
# FILA DE PRIORIDADE
# =========================

class FilaPrioridade:
    def __init__(self):
        self.fila = []
        self.contador = 0

    def enqueue(self, cliente, prioridade):
        heapq.heappush(
            self.fila,
            (prioridade, self.contador, cliente)
        )
        self.contador += 1

    def dequeue(self):
        if self.fila:
            return heapq.heappop(self.fila)

    def empty(self):
        return len(self.fila) == 0


# =========================
# GERANDO 20 CLIENTES
# =========================

clientes = []

for i in range(1, 21):
    nome = f"Cliente {i}"
    senha = f"{i:03}"
    prioridade = random.randint(1, 3)

    clientes.append((nome, senha, prioridade))


print("================================")
print("       20 CLIENTES GERADOS")
print("================================")

for nome, senha, prioridade in clientes:
    print(nome, "- Senha:", senha, "- Prioridade:", prioridade)


# =========================
# FILA CLÁSSICA
# =========================

fila = Fila()

for cliente in clientes:
    fila.enqueue(cliente)

print("\n================================")
print("       FILA CLÁSSICA")
print("================================")

print("Ordem de atendimento:")

while not fila.empty():
    nome, senha, prioridade = fila.dequeue()
    print(nome, "- Senha:", senha)


# =========================
# FILA CIRCULAR
# =========================

fila_circular = FilaCircular()

print("\n================================")
print("       FILA CIRCULAR")
print("================================")

for cliente in clientes:

    # Se estiver cheia, atende o primeiro
    if fila_circular.tamanho == 5:
        atendido = fila_circular.dequeue()

        print(
            "Atendendo:",
            atendido[0],
            "- front:", fila_circular.front,
            "- rear:", fila_circular.rear
        )

    # Coloca um novo cliente
    fila_circular.enqueue(cliente)

    print(
        "Entrou:",
        cliente[0],
        "- front:", fila_circular.front,
        "- rear:", fila_circular.rear
    )


# =========================
# FILA DE PRIORIDADE
# =========================

fila_prioridade = FilaPrioridade()

for cliente in clientes:
    nome, senha, prioridade = cliente

    fila_prioridade.enqueue(
        (nome, senha),
        prioridade
    )

print("\n================================")
print("       FILA DE PRIORIDADE")
print("================================")

print("Ordem de atendimento:")

while not fila_prioridade.empty():

    prioridade, contador, cliente = fila_prioridade.dequeue()

    nome, senha = cliente

    print(
        nome,
        "- Senha:", senha,
        "- Prioridade:", prioridade
    )


# =========================
# COMPARAÇÃO
# =========================

print("\n================================")
print("          COMPARAÇÃO")
print("================================")

print("Fila clássica:")
print("- Atende na ordem de chegada.")

print("\nFila circular:")
print("- Possui capacidade limitada.")
print("- Reutiliza as posições liberadas.")

print("\nFila de prioridade:")
print("- Prioridade 1 é atendida primeiro.")
print("- Depois prioridade 2.")
print("- Depois prioridade 3.")
