"""Ejercicio 2 - Portero de discoteca¶
Escribe un programa que simule el trabajo de un portero de discoteca. El programa debe pedir al usuario su edad y
determinar si puede entrar o no. Si la edad es menor de 18 años, el programa debe imprimir "No puedes entrar".
Si la edad es mayor o igual a 18 años, el programa debe imprimir "Puedes entrar"."""

edad = int(input("Indicame tu edad: "))

if edad >= 18 and edad <= 60:
    print("Puedes pasar")
elif edad > 60:
    print("Vete a la oldSchooldiscotek")
elif edad >= 16:
    print("Vete a KinderGarden")
else:
    print("Vete a tu casa")