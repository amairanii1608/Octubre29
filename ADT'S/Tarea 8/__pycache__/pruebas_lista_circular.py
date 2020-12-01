from listacircular import CircularList

lc= CircularList()
print("Esta vacia?: " , lc.is_empty() )


lc.append(10)
lc.append(20)
lc.append(30)
lc.append(40)

lc.preppend(5)

lc.transversal()

lc.search(50)
lc.search(10)
