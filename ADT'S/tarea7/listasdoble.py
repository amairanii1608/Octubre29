class NodoDoble:
     def __init__( self , value , siguiente =None , anterior=None ):
         self.data = value
         self.next= siguiente
         self.prev=anterior

class DoubleLinkendList:
     def __init__( self ):
         self.__head=NodoDoble( None , None , None )
         self.__tail=NodoDoble( None , None , None )
         self.__head.next=self.__tail
         self.__tail.prev=self.__head
         self:__size=0
         print(f"head : {self.__head}")
         print(f"tail : {self.__tail}")

     def get_size(self):
         return self.__size

     def is_empty( self):
         return self.__head==None

     def append(self, value):
         nuevo=NodoDoble(value)
         if self.is_empty():
           self.__head=self.tail=nuevo
         else:
             while curr_node.next !=None:
                 curr_node=curr_curr_node.next
             curr_nuevo=self.__tail
             self.__tail=curr_node.next=nuevo
             self.__tail.prev=curr_nuevo
          self.__size+=1

     def transversal( self ):
         curr_node = self.__head.next
         while curr_node.next != None:
             print(f" { curr_node.data } --> " , end="")
             curr_node = curr_node.prev
         print(" ")

     def  reverse_transversal( self):
          urr_node=self.__tail.prev
          while curr_node.prev!=None:
              print(f" { curr_node.data } --> " , end="")
              curr_node = curr_node.prev
        print("")

     def find_from_head( self, value):
         curr_node=self.__head
         buscar=None
         while curr_node.next !=None:
             if curr_node.data==value:
                 buscar=curr_node
             curr_node=curr_node.next
         return buscar

    def find_from_tail( self, value):
         curr_node=self.__tail
         buscar=None
         while curr_node.prev !=None:
             if curr_node.data==value:
                  buscar=curr_node
               curr_node=curr_node.prev
         return buscar

      def remove_from_head(self, value):
         curr_node=self.find_from_head(value)
         curr_node !=None:
         curr_node.prev.next=curr_node.next
         curr_node.next.prev=curr_node.prev
         curr_node=None
         self._-size-=1

    def remove_from_tail(self, value):
         curr_node=self.find_from_tail(value)
         curr_node !=None:
         curr_node.prev.next=curr_node.next
         curr_node.next.prev=curr_node.prev
         curr_node=None
         self._-size-=1
