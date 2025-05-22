'''Ejercicio 2 - Contar elementos de una lista¶
Escribe un programa que pida al usuario una lista de palabras separadas por comas y cuente cuántas palabras hay en la
lista. El programa debe imprimir el resultado.
'''
lista_string = input("Escriba la lista de compras separadas por coma: ").split(",")
print(f"La lista tiene {len(lista_string)} palabras")