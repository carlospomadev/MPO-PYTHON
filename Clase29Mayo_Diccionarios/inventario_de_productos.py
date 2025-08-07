'''
Ejercicio 3 - Inventario de productos¶
Escribe un programa que gestione un inventario de productos utilizando un diccionario. El programa debe permitir al
usuario añadir productos con su nombre y cantidad, eliminar productos, y consultar la cantidad de un producto específico.
El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".

'''

inventario = {}
opcion = -1

while opcion != 4:
    print("Escoge una opción:")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Consultar producto")
    print("4.Salir")
    opcion = int(input("Introduce una opción: "))

    if opcion == 1:
        nombre = input("Introduce un producto: ")


