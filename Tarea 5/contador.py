"""
Ejercicio 2
En este ejercicio deberás crear un script llamado contador.py que realice varias tareas sobre un fichero llamado contador.txt 
que almacenará un contador de visitas (será un número):
Nuestro script trabajará sobre el fichero contador.txt. Si el fichero no existe o está vacío lo crearemos con el número 0. 
Si existe simplemente leeremos el valor del contador.
Luego a partir de un argumento:
Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.
Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.
Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla.
Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.
Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: Error: Fichero corrupto.
 
contador.py Ejecución Resultado:

1
2
1
2
"""

from io import open

contador = 0
fichero = open('contador.txt', 'a+')
fichero.seek(0)
datos = fichero.readlines()
print(datos)
print (len(datos))

if len(datos) == 0:
    #fichero = open('contador.txt', 'a+')
    fichero.write(str (contador) + '\n')
    accion = input ("Ingrese la accion a realizar (inc) para incrementar o (dec) para decrementar: ")
    try:
        
        if accion == 'inc':
            contador += 1
            fichero = open('contador.txt', 'a')
            fichero.write(str(contador)+'\n')
            print(contador)

        if accion == 'dec' or accion == 'DEC':
            contador -= 1
            fichero = open('contador.txt', 'a')
            fichero.write(str(contador)+'\n')
            print(contador)
        fichero.close()

    except Exception as e:
        print(f"Error: Fichero Corrupto.", e.__class__)

if len (datos) > 0:

    accion = input ("Ingrese la accion a realizar (inc) para incrementar o (dec) para decrementar: ")
    try:
        
        if accion == 'inc':
            contador = int (datos[len(datos)-1])
            print(contador)
            contador += 1
            fichero = open('contador.txt', 'a')
            fichero.write(str(contador)+'\n')
            print(contador)

        if accion == 'dec' or accion == 'DEC':
            contador = int(datos[len(datos)-1])
            contador -= 1
            fichero = open('contador.txt', 'a')
            fichero.write(str(contador)+'\n')
            print(contador)
        fichero.close()

    except Exception as e:
        print(f"Error: Fichero Corrupto.", e.__class__)