class NodoArbol:
    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

def infija(r):
        if r is not None:
            infija(r.left)
            print(r.data)
            infija(r.right)

def prefija(r):
        if r is not None:
            print(r.data)
            infija(r.left)
            infija(r.right)

def posfija(r):
        if r is not None:
            posfija(r.left)
            posfija(r.right)
            print(r.data)


def main():
        print("Árbol 1")
        arbolu = NodoArbol("+",NodoArbol("-",NodoArbol(5),NodoArbol(4)),NodoArbol("*",NodoArbol(3),NodoArbol(2)))
        print("INFIJA. Recorre primero el hijo izquierdo, despues se va a la raíz y termina con el hijo derecho")
        infija(arbolu)
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("PREFIJA. Recorre primero la raíz, despues el hijo izquierdo, y termina con el hijo derecho")
        prefija(arbolu)
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("POSFIJA. Recorre primero el hijo izquierdo, despues el hijo derecho y termina con la raíz")
        posfija(arbolu)
        print("--------------------------------------------------------")
        print("Árbol 2")
        arbold = NodoArbol(40,NodoArbol(30,NodoArbol(25),NodoArbol(35)),NodoArbol(50,NodoArbol(45),NodoArbol(60)))
        print("INFIJA. Recorre primero el hijo izquierdo, despues se va a la raíz y termina con el hijo derecho")
        infija(arbold)
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("PREFIJA. Recorre primero la raíz, despues el hijo izquierdo, y termina con el hijo derecho")
        prefija(arbold)
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("POSFIJA. Recorre primero el hijo izquierdo, despues el hijo derecho y termina con la raíz")
        posfija(arbold)

main()
