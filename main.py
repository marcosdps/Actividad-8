from clase import Conjunto
import os


def opciones():
    print("""\n------MENU DE OPCIONES-------
-1- Union de conjuntos
-2- Diferencia entre los conjuntos
-3- Evaluar igualdad de conjuntos
-0- SALIR
""")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def menu():
    opcion = opciones()
    while opcion != 0:
        os.system("cls") 
        match opcion:
            case 1: 
                conjuntoUno.mostrarElementos()
                conjuntoDos.mostrarElementos()
                unionConjuntos = conjuntoUno + conjuntoDos
                print("El conjunto union es: ",unionConjuntos)
            case 2:
                conjuntoUno.mostrarElementos()
                conjuntoDos.mostrarElementos()
                difConjuntos = conjuntoUno - conjuntoDos 
                print("La diferencia entre los conjuntos es: ",difConjuntos)
            case 3:
                conjuntoUno.mostrarElementos()
                conjuntoDos.mostrarElementos()
                if conjuntoUno == conjuntoDos:
                    print("Los conjuntos son iguales")
                else: print("Conjuntos distintos")     
        opcion = opciones()

def lecturaConjuntos():
    datos = input("Ingrese los elementos del conjunto separados por coma: ")
    datos = datos.split(",")
    conjunto= list(map(int,datos)) #convierte la lista datos a entero y luego lista guarda esos datos en una lista
    return conjunto
    

if __name__ == "__main__":
    conjuntoUno = Conjunto(lecturaConjuntos())
    conjuntoDos = Conjunto(lecturaConjuntos())
    menu()