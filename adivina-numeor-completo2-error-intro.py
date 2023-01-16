
# Aquí te dejo un ejemplo de un programa en Python que permite al usuario adivinar un número dentro de una secuencia de 1 a 10, tiene una opción para salir del juego, pregunta si desea seguir jugando después de adivinar el número y muestra el número correcto al usuario cuando adivina:

import random

while True:
    number_to_guess = random.randint(1, 10)
    while True:
        user_guess = input(
            "Adivina el número (1-10) o escribe 'salir' para terminar el juego: ")
        if user_guess == "salir":
            print("¡Hasta luego! Gracias por jugar.")
            exit()
        elif int(user_guess) == number_to_guess:
            print(
                "¡Enhorabuena, has adivinado el número! El numero correcto es: ", number_to_guess)
            break
        else:
            print("Lo siento, el número no es correcto. Inténtalo de nuevo.")
    user_continue = input("¿Deseas seguir jugando? (S/N)")
    if user_continue.upper() == "N":
        print("¡Hasta luego! Gracias por jugar.")
        break
