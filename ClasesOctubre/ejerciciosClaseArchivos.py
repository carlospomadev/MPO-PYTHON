"""
Vamos a realizar un programa que lea el archivo sistema_log_extenso.txt e imprima copie en otro errores.txt todos los
mensajes del tipo ERROR
"""

log = open("sistema_log_extenso.txt", "r") #Referencia al archivo
log_errores = open("errores.txt", "w")
log_data = log.readlines() #Lista con todas las lineas en String

for line in log_data:
    if "ERROR" in line:
        log_errores.write(line)