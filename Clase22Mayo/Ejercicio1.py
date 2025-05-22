'''Ejercicio 1 - Sumar elementos de una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados por comas y calcule la suma de todos los
elementos de la lista. El programa debe imprimir el resultado.'''

lista_numero = input("Escribe una lista de números separado por coma:").split(",")
resultado = 0

for numero in lista_numero:
    resultado += int(numero)
print(f"Resultado: {resultado}")


