# Entiendo, para que el juego termine cuando el usuario escribe "salir" en lugar de un número, se puede agregar una condición adicional dentro del except ValueError para comprobar si el valor ingresado es "salir" y en ese caso terminar el juego.

# Aquí te dejo un ejemplo del código modificado:


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
