'''
Ejercicio 3 - Mayor y menor elemento de una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados por comas y encuentre el mayor y el menor
 elemento de la lista. El programa debe imprimir ambos resultados.
'''
lista_numeros = input("Escribe una lista de números separado por coma:").split(",")
lista_numeros = [int(num) for num in lista_numeros]
numero_mayor = max(lista_numeros)
numero_menor = min(lista_numeros)

print(f"El numero menor es: {numero_menor} y el mayor es: {numero_mayor}")