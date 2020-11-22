#Ejercicio 6
#Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
#Nombre Apellido ha sacado un Nota de nota.

cadena = "zeréP nauJ,01"

cad_correcta = cadena [::-1]
print(cad_correcta)

print("{} ha sacado una Nota de: {}".format(cad_correcta[3:],cad_correcta[0:3]))

#Prueba
#Prueba 2
