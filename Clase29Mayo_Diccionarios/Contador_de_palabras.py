'''
Ejercicio 2 - Contar palabras en un texto¶
Escribe un programa que pida al usuario un texto y cuente cuántas veces aparece cada palabra en el texto. El programa
debe imprimir un diccionario donde las claves son las palabras y los valores son sus respectivas frecuencias. Ignora
la puntuación y considera las palabras en minúsculas.

Hola que tal, que cuentas
hola:1
que: 2
tal: 1
cuentas:1


'''

palabras = {}
texto = input("Introduce una frase\n").lower().split()

for palabra in texto:
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1
print(palabras)