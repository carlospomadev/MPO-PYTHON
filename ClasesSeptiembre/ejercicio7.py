frase = input("Escribe la frase: \n")
total_caracteres = len(frase)
lista = frase.split()
num_palabras = len(lista)
palabra_max = ""

for palabra in lista:
    if (len(palabra) > len(palabra_max)):
        palabra_max = palabra

print(f"Número de caracteres: {total_caracteres}")
print(f"Número de palabras: {num_palabras}")
print(f"Palabra mas larga: {palabra_max}")
