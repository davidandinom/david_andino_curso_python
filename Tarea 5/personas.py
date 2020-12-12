"""Ejercicio 1
En este ejercicio deberás crear un script llamado personas.py que lea los datos de un fichero de texto, 
que transforme cada fila en un diccionario y lo añada a una lista llamada personas.
Luego rocorre las personas de la lista y para cada una muestra de forma amigable todos sus campos.
El fichero de texto se denominará personas.txt y tendrá el siguiente contenido en texto plano (créalo previamente):
1;Carlos:Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006
Los campos del diccionario serán por orden: id, nombre, apellido y nacimiento.
Importante
Si quieres leer un fichero que no se ha escrito directamente con Python, 
entonces es posible que encuentres errores de codificación al mostrar algunos caracteres. 
Asegúrate de indicar la codificación del fichero manualmente durante la apertura como argumento en el open, 
por ejemplo con UTF-8:
Resultado
(id=1) Cárlos Peralta => 05/01/1989 
(id=2) Manuel Heredia => 26/12/1973 
(id=3) Rosa Campos => 12/06/1961 
(id=4) David García => 25/07/2006 
"""
from io import open
import time

personas = []
#Apertura del archivo
fichero = open('personas.txt','r', encoding="utf8") #encoding se utiliza para leer caracteres especiales
lineas = fichero.readlines() #Se lee todas las líneas
fichero.close()
print("Le lectura de las lineas del fichero personas.txt queda de la siguiente manera: \n",lineas)

for linea in lineas:
    linea_nueva1 = linea.replace("\n","")  #Reemplazamos todas los saltos de linea por un caracter vacío
    print ("Las lineas sin en \\n quedarias así: ", linea_nueva1)
    linea_nueva2 = linea_nueva1.split(';') #Hacemos la lista de cada línea
    print("La lista de cada linea quedaria asi: ",linea_nueva2)
    #Creamos el diccionario personas con clave: id, nombre, apellido y nacimiento de cada linea
    persona = {'id':linea_nueva2[0],'nombre':linea_nueva2[1],'apellido':linea_nueva2[2],'fecha':linea_nueva2[3]}
    personas.append(persona)
print("El diccionario personas quedaria así: ",personas)

print("Resolución ejercicio 1 - de ficheros")
#Impresión
for dato in personas:
    print (f"(id = {dato['id']}) {dato['nombre']} {dato['apellido']} => {dato['fecha']}")