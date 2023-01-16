# Teniendo en cuenta lo visto en esta clase, diseña un programa en el cual el usuario  tenga que adivinar un número dentro de una secuencia de 1 a 10. Cuando se pregunte al usuario cuál es el número que está dentro de la secuencia, en el caso de que acierte debéis darle la enhorabuena al usuario por adivinar el número, si no acierta el número se concluye el juego.


import random

number_to_guess = random.randint(1, 10)

while True:
    user_guess = input(
        "Adivina el número (1-10) o escribe 'salir' para terminar el juego: ")
    if user_guess == "salir":
        print("¡Hasta luego! Gracias por jugar.")
        break
    elif int(user_guess) == number_to_guess:
        print("¡Enhorabuena, has adivinado el número!")
        break
    else:
        print("Lo siento, el número no es correcto. Inténtalo de nuevo.")


# En este ejemplo se agrega la opción de escribir "salir" para terminar el juego, se valida si el usuario ingresa esta palabra, si es asi se imprime un mensaje de despedida y se sale del ciclo. Si no es correcto, se valida si el numero es igual al generado aleatoriamente, si es correcto se imprime un mensaje de felicitación y se sale del ciclo, si no es correcto se vuelve a preguntar al usuario.

# ////////////////////////////////////
# ////////////////////////////////////

# import random

# number_to_guess = random.randint(1, 10)

# while True:
#     user_guess = int(input("Adivina el número (1-10): "))
#     if user_guess == number_to_guess:
#         print("¡Enhorabuena, has adivinado el número!")
#         break
#     else:
#         print("Lo siento, el número no es correcto. Inténtalo de nuevo.")

# En primer lugar, se importa la librería random para generar un número aleatorio dentro de la secuencia de 1 a 10 y se guarda en la variable number_to_guess.

# En un ciclo while, se pide al usuario que adivine el número y se guarda en la variable user_guess. Si el número adivinado es igual al número generado aleatoriamente, se imprime un mensaje de felicitación y se sale del ciclo. Si no es correcto, se imprime un mensaje de error y se vuelve a preguntar al usuario.

# Es importante mencionar que este juego no tiene un limite de intentos, si el usuario no adivina el numero, debe de salirse del juego manualmente.
