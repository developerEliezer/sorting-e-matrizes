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

fila = Fila()

clientes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
            "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"]

for cliente in clientes:
    fila.enqueue(cliente)

print("fila Classica")

print("Ordem de chegada:")
print(fila.fila)

print("\nPróximo cliente:", fila.head())
print("Tamanho da fila:", fila.size())
print("Fila vazia?", fila.empty())

print("\nOrdem de atendimento:")

while not fila.empty():
    print("Atendendo:", fila.dequeue())

print("\nFila vazia?", fila.empty())
