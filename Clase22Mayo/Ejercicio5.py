'''
Ejercicio 5 - Invertir una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados por comas y la invierta.
El programa debe imprimir la lista invertida.
'''

lista_numeros = input("Introduce la primera lista de números separada por comas: ").split(",")
lista_numeros = [int(num) for num in lista_numeros]
lista_numeros.reverse()
print(lista_numeros)