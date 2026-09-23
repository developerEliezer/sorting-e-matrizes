import heapq

# ==========================================
# ESTRUTURA DO CLIENTE
# ==========================================
class Cliente:
    def __init__(self, nome, senha, prioridade):
        self.nome = nome
        self.senha = senha
        self.prioridade = prioridade  # 1 = Emergência, 2 = Prioritário, 3 = Normal

    def __repr__(self):
        pri_nome = {1: "Emergência", 2: "Prioritário", 3: "Normal"}.get(self.prioridade, "Normal")
        return f"{self.nome} (Senha: {self.senha} | Prio: {self.prioridade} - {pri_nome})"


# ==========================================
# PARTE 1 — FILA CLÁSSICA (FIFO)
# ==========================================
class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, cliente):
        self.fila.append(cliente)

    def dequeue(self):
        if not self.empty():
            return self.fila.pop(0)

    def head(self):
        if not self.empty():
            return self.fila[0]

    def size(self):
        return len(self.fila)

    def empty(self):
        return len(self.fila) == 0


print("=" * 55)
print("             PARTE 1 — FILA CLÁSSICA (FIFO)         ")
print("=" * 55)

fila = Fila()

clientes_p1 = [
    Cliente("Ana", "S001", 3), Cliente("Bruno", "S002", 1),
    Cliente("Carlos", "S003", 2), Cliente("Daniela", "S004", 1),
    Cliente("Eduardo", "S005", 3), Cliente("Fernanda", "S006", 2),
    Cliente("Gabriel", "S007", 3), Cliente("Helena", "S008", 1),
    Cliente("Igor", "S009", 2), Cliente("Juliana", "S010", 3)
]

for cliente in clientes_p1:
    fila.enqueue(cliente)

print("\n--- Ordem de Chegada (10 Clientes) ---")
for c in fila.fila:
    print(f"  • {c}")

print("\n--- Estado da Fila ---")
print(f"Próximo cliente (head) : {fila.head().nome}")
print(f"Tamanho da fila         : {fila.size()}")
print(f"Fila vazia?             : {fila.empty()}")

print("\n--- Ordem de Atendimento ---")
while not fila.empty():
    print(f"  -> Atendendo: {fila.dequeue().nome}")

print(f"\nFila vazia após atendimento? {fila.empty()}")


# ==========================================
# PARTE 2 — FILA CIRCULAR
# ==========================================
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


print("\n" + "=" * 55)
print("             PARTE 2 — FILA CIRCULAR                ")
print("=" * 55)

fila_circ = FilaCircular()

fila_circ.enqueue(Cliente("Ana", "S001", 3))
fila_circ.enqueue(Cliente("Bruno", "S002", 1))
fila_circ.enqueue(Cliente("Carlos", "S003", 2))
fila_circ.enqueue(Cliente("Daniela", "S004", 1))
fila_circ.enqueue(Cliente("Eduardo", "S005", 3))

print("\n--- Fila Inicial (Capacidade Max: 5) ---")
print("  Buffer:", [c.nome if c else None for c in fila_circ.fila])
print(f"  Ponteiros -> Front: {fila_circ.front} | Rear: {fila_circ.rear}")

print("\n--- Atendimento (2 Remoções) ---")
c1 = fila_circ.dequeue()
c2 = fila_circ.dequeue()
print(f"  -> Atendendo: {c1.nome if c1 else None}")
print(f"  -> Atendendo: {c2.nome if c2 else None}")

print("\n--- Estado após remoções ---")
print("  Buffer:", [c.nome if c else None for c in fila_circ.fila])
print(f"  Ponteiros -> Front: {fila_circ.front} | Rear: {fila_circ.rear}")

fila_circ.enqueue(Cliente("Fernanda", "S006", 2))
fila_circ.enqueue(Cliente("Gabriel", "S007", 3))

print("\n--- Estado após reutilizar posições (Inseridos: Fernanda, Gabriel) ---")
print("  Buffer:", [c.nome if c else None for c in fila_circ.fila])
print(f"  Ponteiros -> Front: {fila_circ.front} | Rear: {fila_circ.rear}")


# ==========================================
# PARTE 3 — FILA DE PRIORIDADE
# ==========================================
class FilaPrioridade:
    def __init__(self):
        self.fila = []
        self.contador = 0

    # Adiciona o cliente na fila de prioridade
    def enqueue(self, cliente):
        heapq.heappush(self.fila, (cliente.prioridade, self.contador, cliente))
        self.contador += 1

    # Remove o cliente com maior prioridade
    def dequeue(self):
        if self.fila:
            return heapq.heappop(self.fila)

    # Verifica se a fila está vazia
    def empty(self):
        return len(self.fila) == 0


print("\n" + "=" * 55)
print("             PARTE 3 — FILA DE PRIORIDADE           ")
print("=" * 55)

fila_prio = FilaPrioridade()

clientes_p3 = [
    Cliente("Ana", "S001", 3),
    Cliente("Bruno", "S002", 1),
    Cliente("Carlos", "S003", 2),
    Cliente("Daniela", "S004", 1),
    Cliente("Eduardo", "S005", 3)
]

for c in clientes_p3:
    fila_prio.enqueue(c)

print("\n--- Ordem de Chegada ---")
for c in clientes_p3:
    pri_nome = {1: "Emergência", 2: "Prioritário", 3: "Normal"}.get(c.prioridade)
    print(f"  • {c.nome:<8} - Prioridade {c.prioridade} ({pri_nome})")

print("\n--- Ordem de Atendimento (Por Prioridade) ---")
while not fila_prio.empty():
    prioridade, contador, cliente = fila_prio.dequeue()
    pri_nome = {1: "Emergência", 2: "Prioritário", 3: "Normal"}.get(prioridade)
    print(f"  -> Atendido(a): {cliente.nome:<8} | Prioridade: {prioridade} ({pri_nome})")

print("=" * 55)
