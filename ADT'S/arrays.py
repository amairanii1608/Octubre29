class Array:
    def __init__(self , tam ):
        self.__info = [ 0 for x in range(tam)]

    def get_item( self , posicion ):
        dato =-1
        try:
            dato = self.__info[ posicion ]
        except Exception as e:
            print("Error de posicion")
            dato = "Error"
        return dato


    def set_item( self , dato , posicion ):
        try:
            self.__info[ posicion ]= dato
        except Exception as e:
            print("Error de posicion")

    def get_length( self ):
        return len( self.__info )

    def clear( self , dato ):
        self.__info = [ dato for x in range(len(self.__info)) ]

    def __iter__( self ):
        return IteradorArreglo( self.__info )


class IteradorArreglo:
    def __init__( self , arr ):
       self.__arr = arr
       self.__indice = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self.__indice < len(self.__arr):
            dato = self.__arr[self.__indice]
            self.__indice += 1
            return dato
        else:
            raise StopIteration


"""
algo= Array(10)
print(algo.get_item(6363))
algo.set_item(555,3)
print(algo.get_item(3))
print( f"El arreglo tiene { algo.get_length() } elementos" )
algo.clear(777 )
print(algo.get_item(3))
print("-----------")
for x in algo:
    print( x )
print("----Prueba de iterador----")
for x in range(algo.get_length()):
    print(f"{x} -> {algo.get_item(x)}")

"""
class Empleado:
    def __init__( self , num , nom , pat , mat , he ,sb ,anio ):
        self.__numtrab = numt
        self.__nombres = nom
        self.__paterno = pat
        self.__materno = mat
        self.__hextra = he
        self.__sbase = sb
        self.__aingreso = anio

    def set_num_trabajador( self , num):
        self.__numtrab = num

    def get_num_trabajador( self ):
        return self.__numtrab

    def set_nombres( self , nom):
        self.__nombres = nom

    def get_nombres( self ):
        return self.__nombres

    def set_paterno( self , pat):
        self.__paterno = pat

    def get_paterno( self ):
        return self.__paterno

    def set_materno( self , mat):
        self.__materno = mat

    def get_materno( self ):
        return self.__materno

    def set_horas_extra( self , he):
        self.__hextra = he

    def get_horas_extra( self ):
        return self.__hextra

    def set_sueldo_base( self , sb):
        self.__sbase = sb

    def get_sueldo_base( self ):
        return self.__sbase

    def set_anio_ingreso( self , anio):
        self.__aingreso = anio

    def get_anio_ingreso( self ):
        return self.__aingreso

    def calcular_sueldo( self ):
        return (f"Sueldo = {self.__sbase+(self.__hextra*276.5)+((2020-self.__aingreso)*0.03)}")

    def to_string( self ):
        return self.__num_trabajador , self.__nombres , self.__paterno , self.__materno , self.__hextra , self.__sbase , self.__aingreso

   class Sueldos:
    def __
