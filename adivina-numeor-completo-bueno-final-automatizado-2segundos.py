# Para que el programa genere números aleatorios cada 2 segundos en lugar de inmediatamente, se puede utilizar la función sleep() del módulo time. Esta función detiene la ejecución del programa durante el número de segundos especificado como argumento.
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
    time.sleep(2)
print("El tiempo se ha acabado, gracias por jugar.")
