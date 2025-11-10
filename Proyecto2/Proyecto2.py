import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

# Lista para registrar un historial de los comandos realizados
historial = []


def registrar_comando(comando):
    historial.append(comando)


def mostrar_menu():
    print(" *** GESTOR DE ARCHIVOS EN CONSOLA *** \n")
    #funcion os.getcwd() que devuelve una cadena de texto con la ruta del directorio
    print(f"Directorio actual: {os.getcwd()}")
    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Crear un archivo de texto")
    print("4. Escribir texto en un archivo existente")
    print("5. Eliminar un archivo o directorio")
    print("6. Mostrar información de un archivo o carpeta")
    print("7. Navegar al directorio padre")
    print("8. Navegar dentro de una carpeta")
    print("9. Renombrar archivo o carpeta")
    print("10. Mostrar historial de comandos")
    print("11. Salir")
