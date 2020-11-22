#Ejercicio 3
#Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.

#Sugerencia

#Puedes utilizar la funciones sum() y range() para hacerlo más fácil.
#El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.

numeros = list(range(0,101,2))
suma = sum(numeros)
print(f"Los numeros son: \n{numeros}")
print(f"La suma es: {suma}")