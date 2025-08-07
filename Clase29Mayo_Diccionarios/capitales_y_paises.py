'''
Ejercicio 1 - Capitales y países¶
Escribe un programa que almacene en un diccionario las capitales de varios países, se introducirán los datos con la
 forma PAIS-CAPITAL. Esto debe ejecutarse indefinidamente hasta que el usuario introduzca "FIN INSERCIONES".
  El programa debe permitir al usuario consultar la capital de un país introduciendo su nombre. Si el país no está en
   el diccionario, el programa debe informar al usuario.

   Desarrollo

   paises= {
        "España":"Madrid",
        "Francia":"Paris,
   }

   1.Variables
   2.Bucle que lee y registra las entradas del pais-capital
   3. Pedir un pais y mirar si existe en el diccionario
'''

paises = {}
entrada = input("Indica un valor de la forma 'Pais:Capital o escribe FIN INSERCIONES para finalizar\n").lower()

while entrada != "FIN INSERCIONES".lower():
    pais = entrada.split("-")[0]
    capital = entrada.split("-")[1]
    paises[pais] = capital
    entrada = input("Indica un valor de la forma 'Pais:Capital o escribe FIN INSERCIONES para finalizar\n").lower()
print(paises)

pais_usuario = input("Indica el nombre que quieres consultar\n").lower()
if pais_usuario in paises:
    print(f"La capital de {pais_usuario.capitalize()} es {paises[pais_usuario].capitalize()}")
else:
    print("No existe registro en el diccionario")

