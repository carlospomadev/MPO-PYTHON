#---------------------------------
def nuevo_juego():
    respuestas = []
    respuestas_correctas = 0


    for pregunta in preguntas:
        print("\n________________________")
        print(pregunta["pregunta"])
        for i in pregunta["opciones"]:
            print(i)

        respuesta = input("Ingresa la opción (A, B, C, D): ").upper()
        respuestas.append(respuesta)

        respuestas_correctas += revisar_respuesta(pregunta["respuesta_correcta"],respuesta)

    score(respuestas_correctas, respuestas)
#---------------------------------
def revisar_respuesta(respuesta_correcta, respuesta):
    if respuesta == respuesta_correcta:
        print("Respuesta Correcta :)")
        return 1
    else:
        print("Incorrecto :(")
        return 0
#---------------------------------
def score(respuestas_correctas,respuestas):
    print("\n-------------------------")
    print("RESULTADO")
    print("-------------------------")
    print(f"Respuestas Correctas: {respuestas_correctas}/{len(preguntas)}")

    puntaje = int((respuestas_correctas / len(preguntas)) *100)
    print("Puntaje: " + str(puntaje) + "%")

def juega_nuevamente():
    respuesta = input("\nQuieres jugar de nuevo? (Si o No): ").upper()
    return respuesta == "SI"

#---------------------------------
preguntas = [
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


nuevo_juego()
while juega_nuevamente():
    nuevo_juego()

print("Bye!!")

