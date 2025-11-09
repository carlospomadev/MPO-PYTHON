lista_palabras_feas = ["tonto", "feo", "malo"]
lista_frase = input("Escribe la frase: \n")

for p in lista_palabras_feas:
    lista_frase = lista_frase.replace(p,"*"*len(p))
print(lista_frase)