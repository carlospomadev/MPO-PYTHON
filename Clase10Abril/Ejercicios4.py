"""Ejercicio 4 - Múltiplos de 3 y 5¶
Escribe un programa que pida al usuario un número entero y determine si es múltiplo de 3 o de 5. El programa debe
imprimir un mensaje indicando el resultado. Si el número es múltiplo de ambos, debe imprimir "Múltiplo de 3 y 5".
Si no es múltiplo de ninguno, debe imprimir "No es múltiplo de 3 ni de 5"."""

numero = int(input("Escribe un número: "))

if numero % 3 == 0 and numero %5 == 0:
    print("El número es múltiplo de 3 y 5")
elif numero % 3 == 0:
    print("El número es multipl de 3")
elif numero % 5 == 0:
    print("El número es múltiplo de 5")
else:
    print("El número no es multiplo de 3 ni de 5")
