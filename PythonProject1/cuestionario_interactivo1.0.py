
import random

#Preguntas
preguntas_facil = [
    {"pregunta": "¿Cuál es la capital de España?",
     "opciones":["A. Madrid","B. Barcelona","C. Valencia","D. Sevilla"],
     "respuesta_correcta": "A"},
    {"pregunta":"¿Cuántos días tiene una semana?",
     "opciones":["A. 5","B. 6","C. 7","D. 8"],
     "respuesta_correcta": "C"},
    {"pregunta":"¿Cuál es el resultado de 2 + 2?",
     "opciones":["A. 3","B. 4","C. 5","D. 6"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Cuál es el océano más grande del mundo?",
     "opciones":["A. Atlántico","B. Índico","C. Pacífico","D. Ártico"],
     "respuesta_correcta": "C"},
    {"pregunta": "¿Cuál es el color del cielo en un día despejado?",
     "opciones": ["A. Verde","B. Azul","C. Rojo","D. Amarillo"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Cuántas patas tiene una araña?",
     "opciones": ["A. 6","B. 8","C. 10","D. 4"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Cuál es el planeta más cercano al sol?",
     "opciones": ["A. Venus","B. Marte","C. Mercurio","D. Tierra"],
     "respuesta_correcta": "C"},
    {"pregunta": "¿Qué fruta es conocida por tener muchas semillas?",
     "opciones": ["A. Manzana","B. Naranja","C. Fresa","D. Granada"],
     "respuesta_correcta": "D"},
    {"pregunta": "¿Cuál es el idioma oficial de Brasil?",
     "opciones": ["A. Español","B. Portugués","C. Inglés","D. Francés"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Cuál es el animal más rápido del mundo?",
     "opciones": ["A. Guepardo","B. León","C. Tigre","D. Águila"],
     "respuesta_correcta": "A"
     }
]
preguntas_medio = [
    {"pregunta": "¿En qué año llegó el hombre a la Luna?",
     "opciones": ["A. 1965", "B. 1969", "C. 1971", "D. 1975"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Cuál es el símbolo químico del oro?",
     "opciones": ["A. Au", "B. Ag", "C. Fe", "D. Hg"],
     "respuesta_correcta": "A"},
    {"pregunta": "¿Quién escribió 'Cien años de soledad'?",
     "opciones": ["A. Pablo Neruda", "B. Gabriel García Márquez", "C. Mario Vargas Llosa", "D. Isabel Allende"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Cuál es el país con más habitantes en el mundo?",
     "opciones": ["A. India", "B. Estados Unidos", "C. China", "D. Rusia"],
     "respuesta_correcta": "C"},
    {"pregunta": "¿En qué año llegó Cristóbal Colón a América?",
     "opciones": ["A. 1492","B. 1500","C. 1485","D. 1498"],
     "respuesta_correcta": "A"},
    {"pregunta": "¿Cuál es la fórmula química del agua?",
     "opciones": ["A. CO2","B. H2O","C. NaCl","D. O2"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Qué país tiene la mayor población del mundo?",
     "opciones": ["A. India", "B. Estados Unidos", "C. Indonesia", "D. China"],
     "respuesta_correcta": "D"},
    {"pregunta": "¿Qué instrumento se utiliza para medir la temperatura?",
     "opciones": ["A. Barómetro","B. Termómetro","C. Altímetro","D. Higrómetro"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Cuál es la montaña más alta del mundo?",
     "opciones": ["A. K2", "B. Everest", "C. Makalu", "D. Kilimanjaro"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Cuál es el continente más grande del mundo?",
     "opciones": ["A. África","B. Asia","C. América","D. Europa"],
     "respuesta_correcta": "B"}
    ]

preguntas_dificil = [
    {"pregunta": "¿Cuál es el elemento químico con el símbolo 'W'?",
     "opciones": ["A. Wolframio", "B. Wolfram", "C. Tungsteno", "D. Todas son correctas"],
     "respuesta_correcta": "D"},
    {"pregunta": "¿Qué matemático es conocido por el último teorema que lleva su nombre?",
     "opciones": ["A. Euclides", "B. Fermat", "C. Gauss", "D. Euler"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
     "opciones": ["A. 1937", "B. 1939", "C. 1941", "D. 1945"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Cuál es la capital de Mongolia?",
     "opciones": ["A. Ulan Bator", "B. Astana", "C. Tiflis", "D. Bishkek"],
     "respuesta_correcta": "A"},
    {"pregunta": "¿Quién propuso la teoría de la relatividad?",
     "opciones": ["A. Isaac Newton","B. Nikola Tesla","C. Albert Einstein","D. Galileo Galilei"],
     "respuesta_correcta": "C"},
    {"pregunta": "¿Qué filósofo escribió 'La república'?",
     "opciones": ["A. Platón","B. Aristóteles","C. Sócrates","D. Epicuro"],
     "respuesta_correcta": "A"},
    {"pregunta": "¿Cuál es la distancia aproximada entre la Tierra y la Luna?",
     "opciones": ["A. 384,400 km","B. 150,000 km","C. 500,000 km","D. 1,000,000 km"],
     "respuesta_correcta": "A"},
    {"pregunta": "¿Qué científico descubrió la penicilina?",
     "opciones": ["A. Alexander Fleming","B. Marie Curie","C. Louis Pasteur","D. Gregor Mendel"],
     "respuesta_correcta": "A"},
    {"pregunta": "¿Cuál es el río más largo del mundo?",
     "opciones": ["A. Amazonas","B. Nilo","C. Yangtsé","D. Misisipi"],
     "respuesta_correcta": "B"},
    {"pregunta": "¿Qué artista pintó 'La noche estrellada'?",
     "opciones": ["A. Picasso","B. Van Gogh","C. Monet","D. Da Vinci"],
     "respuesta_correcta": "B"}

]
ranking = []

#funciones
def nuevo_juego(nombre, preguntas):
    respuestas_correctas = 0

    print(f"\nBienvenido/a {nombre}!")
    print("Empecemos el test...")

    #Hacer random las preguntas
    preguntas_random = random.sample(preguntas,len(preguntas))

    for pregunta in preguntas_random:
        print("\n________________________")
        print(pregunta["pregunta"])
        for i in pregunta["opciones"]:
            print(i)

        #validación de entrada
        respuesta = input("Ingresa la opción (A, B, C, D): ").upper()
        while respuesta not in ["A", "B", "C", "D"]:
            respuesta = input("Opción no válida. Ingresa A, B, C, D: ").upper()

        respuestas_correctas += revisar_respuesta(pregunta["respuesta_correcta"],respuesta)

    score(respuestas_correctas, nombre, preguntas)
#---------------------------------
def revisar_respuesta(respuesta_correcta, respuesta):
    if respuesta == respuesta_correcta:
        print("Respuesta Correcta :)")
        return 1
    else:
        print("Incorrecto :(")
        return 0

#---------------------------------
def score(respuestas_correctas,nombre, preguntas):
    print("\n-------------------------")
    print("RESULTADO")
    print("-------------------------")
    print(f"Respuestas Correctas: {respuestas_correctas}/{len(preguntas)}")

    puntaje = int((respuestas_correctas / len(preguntas)) * 100)
    print("Puntaje: " + str(puntaje) + "%")

    #valoración según puntaje
    if puntaje == 100:
        print("Excelente eres un genio!")
    elif 50 <= puntaje < 100:
        print("Estás en el camino correcto!")
    else:
        print("Necesitas practicar! :c")

    #Guardar puntaje
    ranking.append({"nombre": nombre, "puntaje": puntaje})

def mostrar_ranking():
    print("\n***Ranking***")
    if not ranking:
        print("No hay puntajes registrados aún")
    else:
        ranking_ordenado = sorted(ranking, key=lambda x: x["puntaje"], reverse=True)
        for i, jugador in enumerate(ranking_ordenado, start=1):
            print(f"{i}.{jugador["nombre"]} - {jugador["puntaje"]}%")



#Menu Principal
while True:
    print("\n****MENÚ PRINCIPAL****")
    print("1. Empezar test")
    print("2. Ranking")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        nombre_jugador = input("Ingresa tu nombre: ")

        #seleccionar dificultad
        while True:
            print("\nSelecciona dificultad: ")
            print("1. Fácil")
            print("2.Medio")
            print("3.Difícil")

            nivel = input("Opción: ")
            if nivel == "1":
                preguntas = preguntas_facil
                break
            elif nivel == "2":
                preguntas = preguntas_medio
                break
            elif nivel == "3":
                preguntas = preguntas_dificil
                break
            else:
                print("Ingrese una opción válida")

        nuevo_juego(nombre_jugador, preguntas)

    elif opcion == "2":
        mostrar_ranking()

    elif opcion == "3":
        print("Gracias por jugar! Saliendo del test.....")
        break
    else:
        print("Opción no válida, elige 1, 2 o 3")


