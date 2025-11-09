frase = input("Escribe la frase \n")
lista = frase.split()
num_palabras = len(lista)

print(f"Número de palabras: {num_palabras}")
print(f"la primera palabra es: {lista[0]}")
print(f"La última palabra es: {lista[-1]}")