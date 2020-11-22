#Ejercicio 1
#Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

#Si los dos números son iguales
#Si los dos números son diferentes
#Si el primero es mayor que el segundo
#Si el segundo es mayor o igual que el primero

num1 = float (input("Ingrese el primer número: "))
num2 = float (input("Ingrese el primer número: "))

if num1 == num2:
    print ("El número {} es igual al número {}: True".format(num1,num2))
else:
    print ("El número {} es igual al número {}: False".format(num1,num2))

if num1 != num2:
    print ("El número {} no es igual al número {}: True".format(num1,num2))
else:
    print ("El número {} no es igual al número {}: Falso".format(num1,num2))

if num1 > num2:
    print ("El número {} es mayor al número {}: True".format(num1,num2))
else:
    print ("El número {} es mayor al número {}: False".format(num1,num2))

if num2 >= num1:
    print ("El número {} es mayor o igual al número {}: True".format(num2,num1))
else:
    print ("El número {} es mayor o igual al número {}: False".format(num2,num1))