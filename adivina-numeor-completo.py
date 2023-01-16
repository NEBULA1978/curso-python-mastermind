# Teniendo en cuenta lo visto en esta clase, diseña un programa en el cual el usuario  tenga que adivinar un número dentro de una secuencia de 1 a 10. Cuando se pregunte al usuario cuál es el número que está dentro de la secuencia, en el caso de que acierte debéis darle la enhorabuena al usuario por adivinar el número, si no acierta el número se concluye el juego.


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
            print("¡Enhorabuena, has adivinado el número!")
            break
        else:
            print("Lo siento, el número no es correcto. Inténtalo de nuevo.")
    user_continue = input("¿Deseas seguir jugando? (S/N)")
    if user_continue.upper() == "N":
        print("¡Hasta luego! Gracias por jugar.")
        break
