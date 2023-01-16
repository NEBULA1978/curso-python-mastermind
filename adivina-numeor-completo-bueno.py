# Para solucionar el problema de que el programa termine cuando el usuario presiona Enter sin ingresar un número, puedes agregar una validación para comprobar si el valor ingresado es válido antes de compararlo con el número a adivinar.

# Una forma de hacerlo es utilizando un ciclo while y una excepción de tipo ValueError para controlar el caso en el que el usuario no ingresa un número válido. Aquí te dejo un ejemplo:


import random

while True:
    number_to_guess = random.randint(1, 10)
    while True:
        try:
            user_guess = int(
                input("Adivina el número (1-10) o escribe 'salir' para terminar el juego: "))
            break
        except ValueError:
            if user_guess == "salir":
                print("¡Hasta luego! Gracias por jugar.")
                exit()
            print("Por favor ingresa un número válido.")
    if int(user_guess) == number_to_guess:
        print("¡Enhorabuena, has adivinado el número! El numero correcto es: ", number_to_guess)
    else:
        print("Lo siento, el número no es correcto. Inténtalo de nuevo.")
    user_continue = input("¿Deseas seguir jugando? (S/N)")
    if user_continue.upper() == "N":
        print("¡Hasta luego! Gracias por jugar.")
        break
