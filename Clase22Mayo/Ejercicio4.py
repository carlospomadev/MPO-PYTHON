'''Ejercicio 4 - Sumar dos listas de igual longitud¶
Escribe un programa que pida al usuario dos listas de números enteros separados por comas y sume los elementos de ambas
listas. El programa debe imprimir la lista resultante. Si las listas no tienen la misma longitud, el programa debe
imprimir un mensaje de error.
'''

lista1 = input("Introduce la primera lista de números separada por comas: ").split(",")
lista2 = input("Introduce la primera lista de números separada por comas: ").split(",")

if len(lista1) != len(lista2):
    print("La longitud de las listas no es la misma")
else:
    #Defino una lista nueva para el resultado
    suma_listas = []
    #Recorro las dos listas de entrada a la vez con el mismo indice
    for i in range(len(lista1)):
        #Añadir a la última posición de la lista resultado la suma de los valores
        #casteados a entero de esa posici´pn de las listas entrantes
        suma_listas.append(int(lista1[i]) + int(lista2[i]))
        print(suma_listas)
