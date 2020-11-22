#Ejercicio 4
#A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota final. El problema es que cada nota tiene un valor porcentual:

#La primera nota vale un 15% del total
#La segunda nota vale un 35% del total
#La tercera nota vale un 50% del total
#Desarrolla un programa para calcular perfectamente la nota final:

nota_1 = 10
nota_2 = 7
nota_3 = 4

total = nota_1 + nota_2 + nota_3
a = (15 * total) / 100
b = (35 * total) / 100
c = (55 * total) / 100
promedio = (a + b + c) / 3
print ("el promedio es: {}".format(promedio))