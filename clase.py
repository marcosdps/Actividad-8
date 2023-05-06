

class Conjunto:
    __elementos = int


    def __init__(self, elementos={0}):
        self.__elementos = set(elementos) 
        #declaro el elemento como un conjunto, set son conjuntos
        #es un tipo de datos como una lista, pero que no puede repetir datos
            
    def mostrarElementos(self):
        print(self.__elementos)

    def __add__(self, otroConjunto):
        return self.__elementos | otroConjunto.__elementos
    
    def __sub__(self, otroConjunto):
        return self.__elementos - otroConjunto.__elementos
    
    def __eq__(self, otroConjunto):
        return self.__elementos == otroConjunto.__elementos