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


def listar_contenido():
    registrar_comando("Listar contenido")
    print("\nContenido del directorio:")
    try:
        elementos = os.listdir()
        if not elementos:
            print("El directorio está vacío.")
        else:
            tamaño_total = 0
            for elem in elementos:
                ruta = os.path.join(os.getcwd(), elem)
                if os.path.isdir(ruta):
                    print(Fore.BLUE + f"[CARPETA] {elem}")
                elif os.path.isfile(ruta):
                    tamaño_total += os.path.getsize(ruta)
                    print(Fore.GREEN + f"[ARCHIVO] {elem}")

            print(Style.RESET_ALL + f"\nTamaño total de archivos: {tamaño_total} bytes")
    except Exception as e:
        print(f"Error al listar contenido: {e}")


def crear_directorio():
    nombre = input("Nombre del nuevo directorio: ")
    registrar_comando(f"Crear directorio: {nombre}")
    try:
        if os.path.exists(nombre):
            print("Ya existe un archivo o carpeta con ese nombre.")
        else:
            os.mkdir(nombre)
            print("Directorio creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el directorio: {e}")


def crear_archivo():
    nombre = input("Nombre del archivo (con .txt): ")
    registrar_comando(f"Crear archivo: {nombre}")
    try:
        if os.path.exists(nombre):
            print("Ya existe un archivo con ese nombre.")
        else:
            contenido = input("Escribe el contenido inicial: ")
            with open(nombre, "w") as archivo:
                archivo.write(contenido)
            print("Archivo creado con éxito.")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")


def escribir_en_archivo():
    nombre = input("Nombre del archivo: ")
    registrar_comando(f"Escribir en archivo: {nombre}")
    try:
        if not os.path.isfile(nombre):
            print("El archivo no existe.")
        else:
            nuevo_texto = input("Texto para añadir: ")
            with open(nombre, "a") as archivo:
                archivo.write("\n" + nuevo_texto)
            print("El texto se añadió correctamente.")
    except Exception as e:
        print(f"Error al escribir en archivo: {e}")


def eliminar_elemento():
    nombre = input("Nombre del archivo o carpeta a eliminar: ")
    registrar_comando(f"Eliminar: {nombre}")
    try:
        if not os.path.exists(nombre):
            print("No existe el archivo o directorio.")
        else:
            if os.path.isfile(nombre):
                os.remove(nombre)
                print("Archivo eliminado.")
            else:
                os.rmdir(nombre)
                print("Carpeta eliminada.")
    except Exception as e:
        print(f"Error al eliminar: {e}")


def mostrar_informacion():
    nombre = input("Nombre del archivo o carpeta: ")
    registrar_comando(f"Mostrar información: {nombre}")
    try:
        if not os.path.exists(nombre):
            print("No existe ese archivo o carpeta.")
        else:
            tipo = "Carpeta" if os.path.isdir(nombre) else "Archivo"
            #Obtener el tamaño y dfecha de la última modificación
            tamaño = os.path.getsize(nombre)
            fecha = time.ctime(os.path.getmtime(nombre))
            print(f"\nInformación de '{nombre}':")
            print(f"Tipo: {tipo}")
            print(f"Tamaño: {tamaño} bytes")
            print(f"Última modificación: {fecha}")
    except Exception as e:
        print(f"Error al obtener información: {e}")


def navegar_padre():
    registrar_comando("Navegar a directorio padre")
    os.chdir("..")
    print(f"Ahora estás en: {os.getcwd()}")


def navegar_dentro():
    carpeta = input("Nombre de la carpeta a la que deseas entrar: ")
    registrar_comando(f"Navegar dentro: {carpeta}")
    try:
        if not os.path.isdir(carpeta):
            print("No existe una carpeta con ese nombre.")
            return
        os.chdir(carpeta)
        print(f"Ahora estás en: {os.getcwd()}")
    except Exception as e:
        print(f"Error al navegar: {e}")


def renombrar_elemento():
    nombre = input("Nombre actual: ")
    nuevo_nombre = input("Nuevo nombre: ")
    registrar_comando(f"Renombrar {nombre} a {nuevo_nombre}")
    try:
        if not os.path.exists(nombre):
            print("No existe ese archivo o carpeta.")
        else:
            os.rename(nombre, nuevo_nombre)
            print("Renombrado correctamente.")
    except Exception as e:
        print(f"Error al renombrar: {e}")


def mostrar_historial():
    print("\nHistorial de comandos:")
    if not historial:
        print("No se ha registrado ningún comando todavía.")
    else:
        #Recorre la lista de comandos guardados
        for i, cmd in enumerate(historial, 1):
            print(f"{i}. {cmd}")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-11): ")

        if opcion == "1": listar_contenido()
        elif opcion == "2": crear_directorio()
        elif opcion == "3": crear_archivo()
        elif opcion == "4": escribir_en_archivo()
        elif opcion == "5": eliminar_elemento()
        elif opcion == "6": mostrar_informacion()
        elif opcion == "7": navegar_padre()
        elif opcion == "8": navegar_dentro()
        elif opcion == "9": renombrar_elemento()
        elif opcion == "10": mostrar_historial()
        elif opcion == "11":
            print("Saliendo del programa…")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()