import math
""" Ejercicio 1
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y
además explica en un mensaje al usuario la causa y/o solución:
"""
def ejercicio1 (dividendo, divisor):
    resultado = 0.0
    mensaje = ""

    try:
        resultado = dividendo/divisor
    except ZeroDivisionError as zde:
        print("ZeroDivisionError :", zde.__class__)
        mensaje = "No se puede realizar la división por cero\n"
    except Exception as e:
        print("Exception : ", e.__class__)
    else:
        print("La division se realizo correctamente y su resulado es: {}".format(round(resultado,2)))
    return mensaje

"""
Ejercicio 2
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee 
y además explica en un mensaje al usuario la causa y/o solución:
lista = [1, 2, 3, 4, 5]
lista[10]
"""
def ejercicio2 (*args, indice=0):
    dato = -1
    existe = 0

    try:
        if args:
            print("El elemento si existe en la lista")
            dato = args[indice]
            if not dato is None:
                existe = 1
        else:
            print(f" No hay datos en la lista {args}")
    except IndexError as ie:
        print(f" [{type(ie)}]: El elemento con el indice: {indice} no existe en la lista.")
    except Exception as e:
        print(f"Excepcion general del programa", e.__class__)
    
    return dato, existe
"""
Ejercicio 3
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee 
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
colores['blanco']y además explica en un mensaje al usuario la causa y/o solución:
"""

def ejercicio3(diccionario,llave):
    
    try:
        #colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
        dato = diccionario[llave]
        print("El dato con la llave {} es : {}".format(llave, dato))
    except KeyError as ke:
        print("La llave ingresa del diccionario no existe. Error: ", ke.__class__)
    except Exception as e:
        print("Excepcion Global", e.__class__)
    else:
        print(f"El dato con la llave {llave} correcta")

"""
Ejercicio 4
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee 
y además explica en un mensaje al usuario la causa y/o solución:
"""
def ejericicio4 ():

    try:
        suma = 15 + '20'
    except TypeError as te:
        print("No se puede realizar la suma entre un número y un string",te.__class__)
    except Exception as e:
        print(f"Excepcion general del programa", e.__class__)

"""
Ejercicio 5
Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes 
capturar y mostrar este mensaje en su lugar:
Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.
Sugerencia
Puedes utilizar la sintaxis "elemento in lista"
elementos = [1, 5, -2]
# Completa el ejercicio aquí
"""
def agregar_una_vez(lista, elemento):

    try:
        if elemento in lista:
            raise ValueError
        else:
            lista.append(elemento)
    except ValueError as ve:
        print(f"Error: Imposible añadir elementos duplicados => [{elemento}].", ve.__class__)
    except Exception as e:
        print("Excepcion Genral ", e.__class__)
    else:
        print ("Ejecutado correctamente")
    finally:
        print("Este código siempre se ejecuta")

def menu():
    """Presenta el menu principal.
    """
    while True:
        print("""MENU PRINCIPAL TAREA 6
        1.- Ejercicio 1 - División por cero
        2.- Ejercicio 2 - Verificar elemento en una lista
        3.- Ejercicio 3 - Diccionario, busqueda por llave
        4.- Ejercicio 4 - Suma
        5.- Ejercicio 5 - Incrementar elementos en una lista
        S.- Salir 
        """)
        opcion = input("Seleccion la operacion a realizar \n")

        if opcion == '1':
            div = float (input ("Ingrese el dividendo: "))
            divs = float (input ("Ingrese el divisor: "))
            men = ejercicio1(div,divs)
            print (men)

        elif opcion == '2':
            lista = [1, 2, 3, 4, 5]
            print (f"Dada la lista: {lista}")
            index = int(input("Ingresa el indice para buscar un elemento: "))
            dato, existe = ejercicio2(*lista,indice=index)
            print(f"El dato con el indice = {index} es = {dato} ") if existe != 0 else print("Lo sentimos no existe el elemento")

        elif opcion == '3':
            colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
            print (f"El Diccionario es: {colores}")
            llave = 'blanco'
            ejercicio3(colores,llave)

        elif opcion == '4':
            ejericicio4()

        elif opcion == '5':
            lista = [1, 5, -2]
            agregar_una_vez(lista,10)
            agregar_una_vez(lista,8)
            agregar_una_vez(lista,12)
            agregar_una_vez(lista,12)
            agregar_una_vez(lista,8)
            print(lista)

        elif opcion == 'S' or opcion == 's':
            caracter = input("Estas seguro de salir del programa : y/n \n")
            if caracter == 'y' or caracter == 'Y':
                break
        else:
            pass


if __name__ == "__main__":
    menu()
