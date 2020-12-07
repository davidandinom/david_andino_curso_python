""" 
Ejercicio 1
Realiza un programa que siga las siguientes instrucciones:

Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
Crea un conjunto llamado administradores con los administradores Juan y Marta.
Borra al administrador Juan del conjunto de administradores.
Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
Sugerencia

Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista.
También cuentan con un método llamado .discard(elemento) que sirve para borrar o descartar un elemento.

Resultado
Marta es admin
David no es admin
Elvira no es admin
Marcos es admin
Juan no es admin
"""
def ejercicio1():
    usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
    administradores = {"Juan", "Marta"}

    administradores.discard('Juan')
    administradores.add('Marcos')

    for usuario in usuarios:
        if usuario in administradores:
            print(f" El usuario {usuario} es administador")
        else:
            print(f" El usuario {usuario} no es administador")

""" 
Ejercicio 2
Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje
jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

El caballero tiene el doble de vida y defensa que un guerrero.
El guerrero tiene el doble de ataque y alcance que un caballero.
El arquero tiene la misma vida y ataque que un guerrero, 
pero la mitad de su defensa y el doble de su alcance.
Muestra como quedan las propiedades de los tres personajes.
Resultado
Caballero:  {'ataque': 2, 'defensa': 4, 'alcance': 2, 'vida': 4}
Guerrero:   {'ataque': 4, 'defensa': 2, 'alcance': 4, 'vida': 2}
Arquero:    {'ataque': 4, 'defensa': 1.0, 'alcance': 8, 'vida': 2}
"""

def ejercicio2():
    caballero = { 'ataque':2, 'defensa':2, 'alcance': 2, 'vida':2 }
    guerrero  = { 'ataque':2, 'defensa':2, 'alcance': 2, 'vida':2 }
    arquero   = { 'ataque':2, 'defensa':2, 'alcance': 2, 'vida':2 }

    #Primera parte: El caballero tiene el doble de vida y defensa que un guerrero.
    caballero['vida'] = guerrero['vida'] * 2
    caballero['defensa'] = guerrero['defensa'] * 2

    #Segunda parte: El guerrero tiene el doble de ataque y alcance que un caballero.
    guerrero['ataque']  = caballero['ataque']*2
    guerrero['alcance']  = caballero['alcance']*2

    #Tercera condicion : El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
    arquero['vida'] = guerrero['vida']
    arquero['ataque'] = guerrero['ataque']
    arquero['defensa'] = guerrero['defensa']/2
    arquero['alcance'] = guerrero['alcance']*2

    #Resultado
    print("El resultado es: \n")
    print("Caballeros : ",caballero )
    print("Guerrero : ",guerrero )
    print("Arquero : ",arquero )

"""
Ejercicio 3
Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas 
se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).
¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
Sugerencia
Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.
Resultado
==Tareas desordenadas==
6 Distribución
2 Diseño
1 Concepción
7 Mantenimiento
4 Producción
3 Planificación
5 Pruebas

==Tareas ordenadas==
Concepción
Diseño
Planificación
Producción
Pruebas
Distribución
Mantenimiento
"""

def ejercicio3():
    tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
    ]

    print("Tareas desordenadas")
    for tarea in tareas:
        print(tarea[0], tarea[1])
    
    print("\nTareas ordenadas")
    tareas_ordenadas = sorted(tareas)
    for tareaor in tareas_ordenadas:
        print(tareaor[0], tareaor[1])


def menu():
    """Presenta el menu principal.
    """
    while True:
        print("""MENU PRINCIPAL TAREA 6
        1.- Ejercicio 1
        2.- Ejercicio 2
        3.- Ejercicio 3
        S.- Salir 
        """)
        opcion = input("Seleccion la operacion a realizar \n")

        if opcion == '1':
            ejercicio1()

        elif opcion == '2':
            ejercicio2()

        elif opcion == '3':
            ejercicio3()

        elif opcion == 'S' or opcion == 's':
            caracter = input("Estas seguro de salir del programa : y/n \n")
            if caracter == 'y' or caracter == 'Y':
                break
        else:
            pass


if __name__ == "__main__":
    menu()
