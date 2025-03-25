#Creame un diccionary
persona = {
    "nombre" : "Carlos",
    "edad" : 30,
    "registrado" : True
}
print(persona)

#Accedeme a un valor por su clave
print(persona["edad"])

#Añadir nuevas clave-valor

persona["ciudad"] = "Lima"
persona["Numero de hijos"] = 1
print(persona)

#Cambiar el valor de una clave
persona["ciudad"] = "Callao"
persona["Numero de hijos"] = 2
print(persona)

#Eliminar una clave
#del persona["registrado"]
#print(persona)

#Comprobar si una clave ya existe
existe_nombrecito = "nombre" in persona
existe_carlos = "Carlos" in persona["nombre"]
print(existe_nombrecito)
print(existe_carlos)

#Comparar dos valores booleanos
es_menor_y_registrado = persona["edad"]>18 and persona["registrado"]
print(es_menor_y_registrado)

#Usar NOT con un booleano
no_veo_registro = not persona["registrado"]
print(no_veo_registro)

#Creame un conjunto a partir de una lista con duplicados
numeritos = [7,8,4,7,1,2,3,4,5,7,8,9,6,3]

#Convierto a conjunto. porque así elimino duplicidades
conjuntito = set(numeritos)
print(conjuntito)

#Comparar si dos colecciones tienen los mismos elementos únicos.
coleccion_a = set([1,2,2,3])
coleccion_b = set([3,2,1,8
                   ])

mismos_elementos = coleccion_a == coleccion_b
print(mismos_elementos)