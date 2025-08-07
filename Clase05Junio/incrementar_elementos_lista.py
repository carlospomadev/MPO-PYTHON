'''
Ejercicio 7 - Incrementar cada elemento de una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados por comas y un número entero. El programa
 debe definir una función que reciba la lista y el número, incremente cada elemento de la lista por el número dado y
  luego imprima la lista resultante.
'''

def incrementa_lista(lista,numero):
    for i in range(len(lista)):
        lista[i] += numero
    return lista
numeros = input("Introduce una lista de números separados por coma: \n").split()
lista = [int(num) for num in numeros]
numero = int(input("Introduce el incrmeneto: "))
incrementa_lista(lista,numero)
print(lista)