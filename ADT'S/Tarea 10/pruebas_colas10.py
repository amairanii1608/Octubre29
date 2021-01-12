from colas import Queue,BoundedPriorityQueue

print("Pruebas de las colas con prioridad acotada")

maestres = {"prioridad":4, "descripción":"Maestres","personas":["Juan P","Diego H"]}
niños = {"prioridad":2, "descripción":"Niños","personas":["Santi H","Ángel H"]}
mecanicos = {"prioridad":4, "descripción":"Mecánicos","personas":["Diana T","María Z"]}
mujeres = {"prioridad":3 , "descripción":"Mujeres","personas":["Sophia S","Evelyn T"]}
niñas = {"prioridad":1 , "descripción":"Niñas","personas":["Fernanda A","Alejandra R", "Karla P"]}
vigias = {"prioridad":4 , "descripción":"Vigias","personas":["Adriam G","Gabriel S","Humberto Q"]}
timonel = {"prioridad":4 , "descripción":"Timonel","persona":"Gonzalo G"}
hombres = {"prioridad":3 , "descripción":"Hombres","personas":["Christian M", "Gael L","Daniel F"]}
terceraEdad = {"prioridad":2 , "descripción":"3ra edad","personas":["Laura T","Agustina V","Valentin Y"]}
capitan = {"prioridad":5 , "descripción":"Capitan","persona":"Gustavo G"}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(terceraEdad['prioridad'], terceraEdad)
cpa.enqueue(niñas['prioridad'], niñas)
cpa.enqueue(hombres['prioridad'], hombres)
cpa.enqueue(vigias['prioridad'], vigias)
cpa.enqueue(timonel['prioridad'], timonel)
cpa.enqueue(capitan['prioridad'], capitan)

cpa.to_string()
print("")
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
