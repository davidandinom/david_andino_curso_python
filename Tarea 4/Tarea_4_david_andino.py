import math
"""Ejercicio 1
Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a
partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura:
Recordatorio
El área de un rectángulo se obtiene al multiplicar la base por la altura.def area
"""
def area_rectangulo (base, altura):
    """
    Función para calcular área de un rectángulo
    Args:
        base (float): Corresponde a la base del rectángulo
        altura (float): Corresponde a la altura del rectángulo

    Returns:
        area (float): Corresponde al área del rectángulo
    """
    area = base * altura
    return area

"""Ejercicio 2
Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un radio.
Calcula el área de un círculo de 5 de radio:
Recordatorio
El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi.
Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:"""
def area_circulo (radio):
    """
    Función para calcular área de un círculo
    Args:
        radio (float): Corresponde al radio del círculo
    Returns:
        (float): Corresponde al área del rectángulo
    """
    return (radio**2) * math.pi

"""
Ejercicio 3
Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.
Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.
"""
def relacion (a, b):
    """ Función para determinar la relación de dos números
    Args:
        a (float): Primero Número
        b (float): Segundo Número
    Returns:
        (int): Corresponde a la relación entre los números
    """
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

"""
Ejercicio 4
Realiza una función llamada intermedio(a, b) que a partir de dos números, 
devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24:
Recordatorio
El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
"""
def intermedio (a, b):
    """ Función para determinar la relación de dos números
    Args:
        a (float): Primero Número
        b (float): Segundo Número
    Returns:
        (float): Corresponde al número intermedio entre el primer número y el segundo
    """
    return (a + b) / 2

""" Ejercicio 5
Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. 
El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. 
La función tendrá que cumplir lo siguiente:
Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10.
"""
def recortar (numero, minimo, maximo):
    """
    Args:
        numero (float): Número a recortar
        minimo (float): Límite inferior
        maximo (float): Límite superior
    Returns:
        (float): Devuelve el resultado de la comparacion
    """
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero

"""Ejercicio 6
Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares y la segunda con los números impares.
"""
def separar (lista):
    lista_par = []
    lista_impar = []
    for i in lista:
        if i %2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    return lista_par, lista_impar

def menu():
    """Presenta el menu principal.
    """
    while True:
        print("""MENU PRINCIPAL
        1.- Ejercicio 1 - Área rectángulo
        2.- Ejercicio 2 - Área círculo
        3.- Ejercicio 3 - Relación
        4.- Ejercicio 4 - Intermedia
        5.- Ejercicio 5 - Recortar
        6.- Ejercicio 6 - Separar Listas
        S.- Salir 
        """)
        opcion = input("Seleccion la operacion a realizar \n")
        
        if opcion == '1':
           bas_rect = float(input("Ingresa la base del retángulo: "))
           alt_rect = float(input("Ingresa la altura del retángulo: "))
           area_rect = area_rectangulo (bas_rect, alt_rect)
           print ("El área del rectángulo con base {} y altura {} es: {}\n".format (bas_rect, alt_rect, area_rect))

        elif opcion == '2':
            rad_cir = float(input("Ingresa el radio del círculo: "))
            area_cir = area_circulo (rad_cir)
            print (f"El área del del círculo de radio {rad_cir} es: {round(area_cir,2)}\n\n")

        elif opcion == '3':
           num_1 = float(input("Ingresa el primer número: "))
           num_2 = float(input("Ingresa el segundo número: "))
           rel = relacion (a=num_1, b=num_2)
           if rel == 1:
               print (f"La relacion entre el primer número ({num_1}) y el segundo número ({num_2}) es: {rel}")
               print (f"El número {num_1} es mayor que el número {num_2}\n\n")
           elif rel == -1:
               print (f"La relacion entre el primer número ({num_1}) y el segundo número ({num_2}) es: {rel}")
               print (f"El número {num_1} es menor que el número {num_2}\n\n")
           else:
               print (f"La relacion entre el primer número ({num_1}) y el segundo número ({num_2}) es: {rel}")
               print (f"El número {num_1} es igual al número {num_2}\n\n")

        elif opcion == '4':
            num_a = float(input("Ingresa el primer número: "))
            num_b = float(input("Ingresa el segundo número: "))
            num_medio = intermedio (a=num_a, b=num_b)
            print ("El número intermedio entre el número {} y el número {} es:  {}\n\n".format(num_a, num_b, num_medio))

        elif opcion == '5':
            num_recortar = float(input("Ingrese el número a recortar: "))
            lim_minimo = float(input("Ingrese el límite inferior: "))
            lim_maximo = float(input("Ingrese el límite superior: "))
            resultado = recortar (num_recortar, lim_minimo, lim_maximo)
            print ("El resultado de recortar el número {} entre el límite inferior {} y límite superior {} es: {}\n".format(num_recortar,lim_minimo, lim_maximo, resultado))

        elif opcion == '6':
            list_num = []
            n = 1
            cantidad = int (input("Ingrese la cantidad de números a ordenar en listas: "))
            while True:
                if n <= cantidad:
                    num = int(input ("Ingrese los números de la lista: "))
                    list_num.append(num)
                    n += 1
                else:
                    break
            par, impar = separar(list_num)
            print("La lista de números es: ",list_num)
            print ("La lista de números pares es: ",par)
            print ("La lista de números pares es: ",impar)

        elif opcion == 'S' or opcion == 's':
            caracter = input("Estas seguro de salir del programa : y/n \n")
            if caracter == 'y' or caracter == 'Y':
                break
        else:
            pass


if __name__ == "__main__":
    menu()
