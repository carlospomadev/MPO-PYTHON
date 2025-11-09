lista_peliculas = list()
opcion = input("Introduce una pelicula (fin para acabar):\n")
while opcion != "fin":
    lista_peliculas.append(opcion)
    opcion = input("Introduce otra pelicula (fin para acabar):\n")

print(f"Número total de peliculas: {len(lista_peliculas)}")
print(f"La primera pelicula es: {lista_peliculas[0]}")
print(f"la última pelicula es {lista_peliculas[-1]}")
print(f"Número total de peliculas sin repetir{set(lista_peliculas)}")
