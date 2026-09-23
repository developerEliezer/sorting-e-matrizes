import heapq

class FilaPrioridade:
    def __init__(self):
        self.fila = []
        self.contador = 0

    # Adiciona o cliente na fila de prioridade
    def enqueue(self, cliente, prioridade):
        heapq.heappush(self.fila, (prioridade, self.contador, cliente))
        self.contador += 1

    # Remove o cliente com maior prioridade
    def dequeue(self):
        if self.fila:
            return heapq.heappop(self.fila)

    # Verifica se a fila está vazia
    def empty(self):
        return len(self.fila) == 0

fila = FilaPrioridade()

# Cadastro dos clientes e prioridades
fila.enqueue("Ana", 3)
fila.enqueue("Bruno", 1)
fila.enqueue("Carlos", 2)
fila.enqueue("Daniela", 1)
fila.enqueue("Eduardo", 3)

print("Prioridades")

#  ordem dos clientes que chegaram
print("\nOrdem de chegada:")
print("Ana - Prioridade 3")
print("Bruno - Prioridade 1")
print("Carlos - Prioridade 2")
print("Daniela - Prioridade 1")
print("Eduardo - Prioridade 3")

# Ordem de atendimento
print("\nOrdem de atendimento:")

while not fila.empty():
    prioridade, contador, cliente = fila.dequeue()
    print("Atendido(a):", cliente, "- Prioridade:", prioridade)
