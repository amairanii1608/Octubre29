class NodoCircular:
    def __init__ ( self , value , siguiente=None ):
        self.dato = value
        self.next = siguiente

class CircularList:
    def __init__ ( self):
        self.__ref = None
        self.__tail = None
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty( self):
        return self.__ref==None

    def preppend( self, value ):
        if self.is_empty():
            self.__ref = self.__tail = NodoCircular(value)
            self.__tail.next = self.__ref
        else:
            curr_node = NodoCircular(value)
            curr_node.next = self.__ref
            self.__tail = curr_node
            self.__tail.next = self.__ref

    def append(self, value):
        if self.is_empty():
           self.__ref = self.__tail = NodoCircular(value)
           self.__tail.next = self.__ref
        else:
            curr_node = self.__tail
            self.__tail = curr_node.next = NodoCircular(value)
            self.__tail.next = self.__ref

    def remove_from_ref(self):
        if self.is_empty():
            print("La lista esta vacia")
        elif self.__ref == self.__tail:
            self.__ref= self.__tail = None
        else:
            self.__ref = self.__head.next
            self.__tail.next = self.__ref

    def remove_from_tail(self):
        if self.is_empty():
            print("La lista esta vacia")
        elif self.__ref == self.__tail:
            self.__ref = self.__tail = None
        else:
            curr_node = self.__ref
            while curr_node.next != self.__tail:
                curr_node = curr_node.next
            curr_node.next = self.__ref
            self.__tail = curr_node

    def transversal( self ):
        curr_node = self.__ref
        while curr_node.next != self.__ref:
            print(curr_node.dato)
            curr_node = curr_node.next
        print(curr_node.dato)

    def search( self , value ):
        curr_node = self.__ref
        while curr_node.next != self.__ref and value != curr_node.dato:
            curr_node = curr_node.next
        return print(value == curr_node.dato)
