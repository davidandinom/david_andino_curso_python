#"Ejercicio 2
#Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.

while True:
    num1 = int (input("Ingrese un número impar: "))
    if num1 %2 != 0:
        print(f"El número es {num1} es impar")
        break