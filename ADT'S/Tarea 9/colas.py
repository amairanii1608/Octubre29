class Queue:
    def __init__( self ):
        self.__data = list()  # []

    def is_empty( self ):
        return len(self.__data) == 0

    def length( self ):
        return len(self.__data)

    def enqueue( self , elem):
        self.__data.append(elem)

    def dequeue( self ):
        if not self.is_empty():
           return self.__data.pop(0)
        else:
            return None

    def to_string( self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "| " + str( elem )
        cadena = cadena + "|"
        return cadena

class PriorityQueue:
    def __init__( self , niveles):
        self.__data = [ Queue() for x in range(niveles)]
        self.__size = 0

    def is_empty( self):
        return self.__size ==0

    def length( self):
        return self.__size

    def enqueue( self, prioridad, elem):
            self.__data[prioridad].append(elem)

    def dequeue(self):
            for Queue in self.__data:
                try:
                    return Queue.pop(0)
                except IndexError:
                    continue

    def to_string( self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "| " + str( elem )
        cadena = cadena + "|"
        return cadena
