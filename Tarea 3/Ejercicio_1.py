#Ejercicios « Controlando el flujo
#Ejercicio 1
#Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#En caso de introducir una opción inválida, el programa informará de que no es correcta.

num1 = float (input("Ingrese un número: "))
num2 = float (input("Ingrese otro número: "))
while True:
    print("{}\n".format("Menú Principal"),
        "{:15}\n".format("1) Sumar los dos números"),
        "{:15}\n".format("2) Restar los dos números"),
        "{:15}\n".format("3) Multiplicar los dos números"),
        "{:15}\n".format("4) Salir"),
    )
    opcion = input("Seleccione la operación a realizar: ")

    if opcion == '1':
        suma = num1 + num2
        print(f"La suma de {num1} + {num2} es = {suma}")

    elif opcion == '2':
        resta = num1 - num2
        print(f"La resta de {num1} - {num2} es = {resta}")

    elif opcion == '3':
        mul = num1 * num2
        print(f"La multiplicación de {num1} * {num2} es = {mul}")

    elif opcion == '4':
        break
