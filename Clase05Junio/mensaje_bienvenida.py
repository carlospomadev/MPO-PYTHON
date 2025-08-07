'''
Ejercicio 2 - Condigura un mensaje de bienvenida¶
Escribe un programa que pida al usuario un nombre, un apellido y una edad. El programa debe definir una función que
reciba estos datos y luego imprima un mensaje de bienvenida personalizado.
'''

def configurar_mensaje(nombre, apellido,edad):
    print(f"Bienvenid@ {nombre} {apellido} {edad}")

nombre = input("Introduce tu nomnbre: ")
apellido = input("Introduce tu apellido: ")
edad = input("Introduce tu edad: ")

print(configurar_mensaje(nombre,apellido,edad))