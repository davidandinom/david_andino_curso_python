"""
Ejercicio 3
Utilizando como base el ejercicio de los personajes que hicimos, en este ejercicio tendrás que crear un gestor de personajes gestor.py
 para añadir y borrar la información de los siguientes personajes:

 	      Vida	Ataque	Defensa	Alcance
Caballero	4	    2	    4	    2
Guerrero	2	    4	    2	    4
Arquero	    2	    4	    1	    8
Deberás hacer uso del módulo pickle y todos los cambios que realices se irán guardando en un fichero binario personajes.pckl, 
por lo que aunque cerremos el programa los datos persistirán.

Crea dos clases, una Personaje y otra Gestor.
La clase Personaje deberá permitir crear un personaje con el nombre (que será la clase), y sus propiedades de vida, ataque, 
defensa y alcance (que deben ser números enteros mayor que cero obligatoriamente).
Por otro lado la clase Gestor deberá incorporar todos los métodos necesarios para añadir personajes, mostrarlos y borrarlos 
(a partir de su nombre por ejemplo, tendrás que pensar una forma de hacerlo), además de los métodos esenciales para guardar los cambios en el fichero personajes.pckl que se deberían ejecutar automáticamente.
En caso de que el personaje ya exista en el Gestor entonces no se creará.
Una vez lo tengas listo realiza las siguientes prueba en tu código:

Crea los tres personajes de la tabla anterior y añádelos al Gestor.
Muestra los personajes del Gestor.
Borra al Arquero.
Muestra de nuevo el Gestor.
Sugerencia

El ejemplo con pickle que realizamos anteriormente puede servirte como base.
gestor.py
Resultado

Se han cargado 2 personajes
Caballero => 4 vida, 2 ataque, 4 defensa, 2 alcance
Guerrero => 2 vida, 4 ataque, 2 defensa, 4 alcance
Arquero => 2 vida, 4 ataque, 1 defensa, 8 alcance

Personaje Arquero borrado
Caballero => 4 vida, 2 ataque, 4 defensa, 2 alcance
Guerrero => 2 vida, 4 ataque, 2 defensa, 4 alcance
"""
from io import open
import pickle

class Personaje:
     
    def __init__ (self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__ (self):
        return '{} => {} vida, {} ataque, {} defensa, {} alcance'.format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor:
    
    personajes = []
    
    def __init__ (self,personajes = []):
        self.personajes = personajes

    def anadir (self, personaje):
        for p in self.personajes:
            if p.nombre == personaje.nombre:
                print (f"El personaje {personaje.nombre} ya existe")
                return
        self.personajes.append(personaje)
        self.guardar ()

    def mostrar (self):
        for p in self.personajes:
            print ("Los personajes son: ",p)
    
    def borra_personaje (self, personaje_borrar):
        self.personajes.remove(personaje_borrar)
        self.guardar()
        print (f"El personaje {personaje_borrar.nombre} ha sido borrado")

    def guardar (self):
        fichero = open('personajes.pckl', "wb")
        pickle.dump(self.personajes, fichero)
        fichero.close()

if __name__ == "__main__":
    p_1 = Personaje ('Caballero',4,2,4,2)
    p_2 = Personaje ('Guerrero',2,4,2,4)
    p_3 = Personaje ('Arquero',2,4,1,8)

    personaje = Gestor ()
    personaje.anadir(p_1)
    personaje.anadir(p_2)
    personaje.anadir(p_3)
    personaje.anadir(p_3)
    personaje.anadir(p_2)
    personaje.mostrar()
    personaje.borra_personaje(p_3)
    print("Después de Borrar: ")
    personaje.mostrar()

