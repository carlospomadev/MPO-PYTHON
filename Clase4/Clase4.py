#Ejercicio 1: Operaciones numéricas complejas
#Define cinco variables numéricas distintas (int, float, complex) y
# realiza diversas operaciones matemáticas (potenciación, division entera, módulo).
# Imprime los resultados formateados en una cadena clara y descriptiva

#num1, num2, num3, num4, num5 = 10, 3, 2.5, 7.2, 4+2j
#resultado = (f"Potencia: {num1 ** num2}, división entera: {num1 // num2},"
            #f" modulo: {num1%num2}, multiplicación: {num3*num4}, complejo: {num5}")
#print(resultado)

#Ejercicio 2: Combinación de cadenas y números
#Define dos variables numéricas (int, float) y tres cadenas diferentes.
#Genera una nueva cadena combinando texto con el resultado de opeaciones aritméticas entre estas variables
#Usa conversión explícita (str()) para insertar valores numéricos en la cadena final

num_int, num_float = 8, 3.5
cadena1, cadena2, cadena3 = "Resultado:","La suma es ", " y la división es "
resultado = (cadena1 + cadena2 + str(num_int+num_float) + cadena3 + str(num_int/num_float))
print(resultado)

#Ejercicio 3:
#Crea una cadena larga que contenga espaciones en blanco al inicio. final y en medio.
#Realiza varias operaciones encadenadas como eliminar
#espaciones extremos, convertir to_do a mayúsculas,
# y dividir la cadena en varias subcadenas usando un separador específico.

cadena=" esTo es uNa cadEna para manipular "
nueva_cadena = cadena.strip().upper().split()
print(nueva_cadena)