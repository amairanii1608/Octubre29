from colas import Queue,PriorityQueue

print("Pruebas de las colas con prioridad no acotada")

cpna = PriorityQueue()
cpna.enqueue(28)
cpna.enqueue(14)
cpna.enqueue(15)
cpna.enqueue(229)
cpna.enqueue(25)
cpna.enqueue(50)

print(cpna.to_string())
while not cpna.is_empty():
        print(cpna.dequeue())
