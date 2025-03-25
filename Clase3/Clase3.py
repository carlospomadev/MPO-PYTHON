import math
import random

#1. Longitud de una cadena
nombre = "Carlos Poma"
print("Longitud del nombre: ", len(nombre))

#2. Convertir texto a mayusculas y minisculas

#upper
print("Este soy yo en mayúsculas: ", nombre.upper())

#lower
print("Este soy yo en minúscula: ", nombre.lower())
print(nombre)

#3. Slicing
print("Primeros 3 caracteres: ", nombre[:3])
print("Últimos 4 caracteres: ", nombre[-4:])

#4. Reemplazar palabras en una cadena
frase = "Me gusta Java"
print("cambio la palabra: ", frase.replace("Java", "Python"))
print(frase)

#5. Verificar si una cadena existe en otra
print("Python" in frase)
nueva_frase= "Me gusta Python"
print("Python" in nueva_frase)

#6. Unir varias palabras en una cadena
palabras=["Hola","Mundo", "en", "Python"]
print("Frase completa con join: "," " .join(palabras))
print("\n")

#7. Split
oracion="Python es divertido"
palabritas=oracion.split()
print("Lista de palabras de mi grupo: ", palabritas)

#8. Redondear un número decimal
numero = 3.1416
print("Mi numero redondeado es:", round(numero,2))

#9. Formateo de numeros decimales
precio = 19.99
print("precio con dos decimales: {:.2f}".format(precio))

#10. Obtener el valor ASCII de un caracter
print("Esto es el código ASCII de 'A': ", ord('A'))

#11. Elevar al cuadrado
numero_al_cuadrado = 5
print("5 al cuadrado es: ", numero_al_cuadrado ** 2)

#12. Raiz cuadrada
numero = 100
print("Raiz cuadrada de 100: ", math.sqrt(numero) )

#13. Divisiones enteras y resto
print("Dvisión normal: ", 10/3)
print("Dvisión entera: ", 10//3)
print("Resto: ", 10%3)

#14. Generar un número aleatorio
print("Número aleatorio entre 1 al 10: ", random.randint(1,10))

#15. Convertir números a cadenas y viceversa
numerito = 300
texto = str(numerito)
print("Convertir a texto: soy: ", texto)

cadena = "200"
numerito = int(cadena)
print("Convertido a numero soy: ", numerito)

#16. Redondear hacia arriba
print("Redondeo hacia arriba del numero 3.6: ", math.ceil(3.6))
print("Redondeo hacia abajo del numero 3.2: ", math.floor(3.2))

#17. Convertir una lista en un conjunto, es decir, eliminar duplicados
numeroides = [1,2,3,4,5,5]
numeroides_sin_duplicados = set(numeroides)
print("La lista de numeroides sin duplicados es: ", numeroides_sin_duplicados)

#18. Repetir una cadena
print("Python!" * 3)

#19. Tipo de dato
dato = 3.1415
print("El tipo de variable es: ", type(dato))

#20. Combinar cadenas y variables en un print
name = "Carlos"
edad = 30
print(f"Hola, soy {name}. Tengo {edad} años de edad. :P")