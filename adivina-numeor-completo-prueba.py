# Para que el juego también permita salir después de no haber adivinado el número, se puede agregar una pregunta similar a la que se hace al final del juego después de cada intento fallido. De esta forma, si el usuario decide salir después de no haber adivinado el número, el juego termina y se muestra un mensaje de despedida.

# Puedes agregar la pregunta antes de la impresión del mensaje "Lo siento, el número no es correcto. Inténtalo de nuevo." y utilizar una estructura de control de flujo if -else para determinar si el juego continúa o no.

# Aquí te dejo un ejemplo de como podria ser el codigo modificado:

import random

while True:
    number_to_guess = random.randint(1, 10)
    while True:
        user_guess = input(
            "Adivina el número (1-10) o escribe 'salir' para terminar el juego: ")
        if user_guess.lower() == "salir":
            print("¡Hasta luego! Gracias por jugar.")
            exit()
        try:
            user_guess = int(user_guess)
            break
        except ValueError:
            print("Por favor ingresa un número válido.")
    if user_guess == number_to_guess:
        print("¡Enhorabuena, has adivinado el número! El numero correcto es: ", number_to_guess)
        user_continue = input("¿Deseas seguir jugando? (S/N)")
        if user_continue.upper() == "S":
            continue
        else:
            break
    else:
        print("Lo siento, el número no es correcto. Inténtalo de nuevo.")
