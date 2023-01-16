# Entiendo, para que el programa introduzca números automáticamente, se pueden utilizar las funciones randint() y randrange() del módulo random para generar números aleatorios en lugar de pedir al usuario que ingrese un número.
# Y para que el programa siga jugando automáticamente durante 5 minutos, podríamos utilizar un bucle while con un contador de tiempo que se detiene al alcanzar el tiempo establecido, y dentro del bucle, generar números aleatorios y compararlos con el número a adivinar.

# Aquí te dejo un ejemplo de cómo podría ser el código modificado:


import random
import time

start_time = time.time()
end_time = start_time + 300  # 5 minutos en segundos
number_to_guess = random.randint(1, 10)

while time.time() < end_time:
    user_guess = random.randint(1, 10)
    if user_guess == number_to_guess:
        print("¡Enhorabuena, se ha adivinado el número correcto es: ", number_to_guess)
        number_to_guess = random.randint(1, 10)
    else:
        print("El número generado: ", user_guess,
              " no es correcto. Inténtalo de nuevo.")
print("El tiempo se ha acabado, gracias por jugar.")
