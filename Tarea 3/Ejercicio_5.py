#Ejercicio 5
#Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
#Concepto útil
#La sintaxis [valor] in [lista] permite comprobar si un valor se encuentra en una lista (devuelve True o False).

numero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    num = int (input("Ingrese el número entre 0 y 9: "))
    if num >=0 and num <=9:
        break

while num in numero:
    print("Número correcto")
    break
else:
    print("Número incorrecto")