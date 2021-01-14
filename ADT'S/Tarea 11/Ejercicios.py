print("Ejemplo clase")
def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)

def main():
    datos= [4,2,3,5] #14
    res=suma_lista_rec(datos)
    print(res)
main()
print("\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

print("Ejercicio 1")
def CuentaReg(num):
    num -= 1
    if num >= 0:
        print(num)
        CuentaReg(num)
    else:
        pass

def main2():
    num=9
    print(f"Numero: {num}")
    CuentaReg(num)
main2()
print("\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

#print("Ejercicio 2")
#def eliminar(elemento):
#    p =+ 1
#    if (p.is_empty() == True or p.length() <= 2):
#        return
#    pm = p.peek()
#    p.pop()

#from stack import Stack
#def main3():

#main3()
