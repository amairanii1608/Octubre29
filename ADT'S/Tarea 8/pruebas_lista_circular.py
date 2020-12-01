from listacircular import CircularList

lc= CircularList()
print("Esta vacia?: " , lc.is_empty() )

lc.insert_in(5)
lc.insert_fi(10)
lc.insert_fi(20)
lc.insert_fi(30)
lc.insert_fi(40)




lc.transversal()

lc.search(50)
lc.search(10)
