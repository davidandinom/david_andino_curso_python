#Ejercicio 2
#Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

#Solución

cadena = str(input(" Ingrese una cedana: "))

if len(cadena) >= 3 and len(cadena) < 10:
    print ("¿La cadena ingresada tiene una longitud mayor o igual que 3 y a su vez es menor que 10? : True")
else:
    print ("¿La cadena ingresada tiene una longitud mayor o igual que 3 y a su vez es menor que 10? : False")