# Para preguntar al usuario si desea seguir jugando después de acertar el número, puedes agregar una pregunta y una validación similar a la que se hace al final del juego dentro del ciclo while que valida si el usuario ha adivinado el número correcto.

# Aquí te dejo un ejemplo de cómo podría quedar el código modificado:
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
        user_continue = input("¿Deseas seguir jugando? (S/N)")
        if user_continue.upper() == "S":
            continue
        else:
            break
    else:
        print("Lo siento, el número no es correcto. Inténtalo de nuevo.")
print("¡Hasta luego! Gracias por jugar.")
