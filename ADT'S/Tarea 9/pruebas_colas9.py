from colas import Queue,PriorityQueue

print("Pruebas de las colas con prioridad no acotada")

cpna = PriorityQueue(7)
print(f"La cola esta vacia?  {cpna.is_empty()}")
print(f"el tamaño de la cola: {cpna.length()}")
cpna.enqueue(5)
cpna.enqueue(15)
cpna.enqueue(10)
cpna.enqueue(1)
cpna.dequeue()
print(cpna.to_string())
while not cpna.is_empty():
        print(cpna.dequeue())
cpna.to_string()
