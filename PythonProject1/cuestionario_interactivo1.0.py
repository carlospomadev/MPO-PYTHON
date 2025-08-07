#---------------------------------
def nuevo_juego():
    respuestas = []
    respuestas_correctas = 0
    preguntas_num = 0

    for key in preguntas:
        print("________________________")
        print(key)
        for i in opciones[preguntas_num]:
            print(i)

        respuesta = input("Ingresa la opción (A, B, C, D: ").upper()
        respuestas.append(respuesta)

        respuestas_correctas += (preguntas.get(key), respuesta)
        preguntas_num += 1
    score()respuestas_correctas,respuesta)
#---------------------------------
def revisar_respuesta(respuesta_correcta, respuesta):
    if respuesta_correcta == respuesta:
        print("Respuesta Correcta :)")
        return 1
    else:
        print("Incorrecto :(")
        return 0
#---------------------------------
def score(respuestas_correctas,respuestas):
    print("-------------------------")
    print("RESULTADO")
    print("-------------------------")
#---------------------------------
def juega_nuevamente():
    pass
#---------------------------------
preguntas = {"¿Cuál es la capital de España?":"A",
             "¿Cuántos días tiene una semana?":"C",
             "¿Cuál es el resultado de 2 + 2?":"B",
             "¿Cuál es el océano más grande del mundo?":"C",
             "¿Cuál es el color del cielo en un día despejado?":"B",
             "¿Cuántas patas tiene una araña?":"B",
             "¿Cuál es el planeta más cercano al sol?":"C",
             "¿Qué fruta es conocida por tener muchas semillas?":"D",
             "¿Cuál es el idioma oficial de Brasil?":"B",
             "¿Cuál es el animal más rápido del mundo?":"A"
}
opciones = [["A. Madrid","B. Barcelona","C. Valencia","D. Sevilla"],
            ["A. 5","B. 6","C. 7","D. 8"],
            ["A. 3","B. 4","C. 5","D. 6"],
            ["A. Atlántico","B. Índico","C. Pacífico","D. Ártico"],
            ["A. Verde","B. Azul","C. Rojo","D. Amarillo"],
            ["A. 6","B. 8","C. 10","D. 4"],
            ["A. Venus","B. Marte","C. Mercurio","D. Tierra"],
            ["A. Manzana","B. Naranja","C. Fresa","D. Granada"],
            ["A. Español","B. Portugués","C. Inglés","D. Francés"],
            ["A. Guepardo","B. León","C. Tigre""D. Águila"]]
nuevo_juego()

