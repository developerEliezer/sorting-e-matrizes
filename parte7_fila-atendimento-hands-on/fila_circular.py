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

fila = FilaCircular()

fila.enqueue("Ana")
fila.enqueue("Bruno")
fila.enqueue("Carlos")
fila.enqueue("Daniela")
fila.enqueue("Eduardo")

print("Fila Circular")

print("\nFila inicial:")
print(fila.fila)
print("front:", fila.front)
print("rear:", fila.rear)

print("\nAtendendo:", fila.dequeue())
print("Atendendo:", fila.dequeue())

print("\nremoções:")
print(fila.fila)
print("front:", fila.front)
print("rear:", fila.rear)

fila.enqueue("Fernanda")
fila.enqueue("Gabriel")

print("\n reutizando posições:")
print(fila.fila)
print("front:", fila.front)
print("rear:", fila.rear)
