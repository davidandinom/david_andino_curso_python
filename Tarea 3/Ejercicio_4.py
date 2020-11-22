#Ejercicio 4
#Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.

cantidad = int((input("Cuántos números quiere introducir: ")))
i = 1
num = 0
datos = []
while True:
    if i <= cantidad:
        num = float (input("Introduce un número: "))
        i += 1
        datos.append(num)
    else:
        break
suma = sum(datos)
media = suma / cantidad
print (f"Se ha introducido {cantidad} números que en total han sumado {suma} y la media es {media}")