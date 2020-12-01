class NodoCircular:
    def __init__ ( self , value , siguiente=None ):
        self.dato = value
        self.next = siguiente

class CircularList:
    def __init__ ( self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty( self):
        return self.__head==None

    def preppend( self, value ):
        if self.is_empty():
            self.__head = self.__tail = NodoCircular(value)
            self.__tail.next = self.__head
        else:
            curr_node = NodoCircular(value)
            curr_node.next = self.__head
            self.__tail = curr_node
            self.__tail.next = self.__head

    def append(self, value):
        if self.is_empty():
           self.__head = self.__tail = NodoCircular(value)
           self.__tail.next = self.__head
        else:
            curr_node = self.__tail
            self.__tail = curr_node.next = NodoCircular(value)
            self.__tail.next = self.__head

    def remove_from_head(self):
        if self.is_empty():
            print("La lista esta vacia")
        elif self.__head == self.__tail:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__tail.next = self.__head

    def remove_from_tail(self):
        if self.is_empty():
            print("La lista esta vacia")
        elif self.__head == self.__tail:
            self.__head = self.__tail = None
        else:
            curr_node = self.__head
            while curr_node.next != self.__tail:
                curr_node = curr_node.next
            curr_node.next = self.__head
            self.__tail = curr_node

    def transversal( self ):
        curr_node = self.__head
        while curr_node.next != self.__head:
            print(curr_node.dato)
            curr_node = curr_node.next
        print(curr_node.dato)

    def search( self , value ):
        curr_node = self.__head
        while curr_node.next != self.__head and value != curr_node.dato:
            curr_node = curr_node.next
        return print(value == curr_node.dato)
