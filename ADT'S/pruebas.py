from arrays import Array

algo= Array(10)
print(f"Get item -> {algo.get_item(6363)}")
print(f"Set item -> {algo.set_item(555, 3)}")
print(f"Get item -> {algo.get_item(3)}")
print(f"El arreglo tiene {algo.get_length()} elementos")
algo.clear(777)
print(f"Get item -> {algo.get_item(3)}")
print("-------------")
for x in algo:
    print( x )
print("\n----Prueba de iterador----")
for x in range(algo.get_length()):
    print(f"{x} -> {algo.get_item(x)}")
