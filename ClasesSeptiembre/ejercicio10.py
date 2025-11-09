correos = input("Introduce una lista de corres separados por coma \n").split(",")
correos_clas = {}

for correo in correos:
    correo_separado = correo.split("@")[1]
    extension = correo_separado.split(".")[0]
    if extension not in correos_clas.keys():
        correos_clas[extension] = list()

    correos_clas[extension].append(correo)
print(correos_clas)