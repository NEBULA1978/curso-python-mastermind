# Para que el programa automáticamente continúe después de 3 segundos si el usuario no responde a la pregunta "¿Deseas salir? (S/N)", se puede utilizar un bucle while dentro del if que verifica si se ha alcanzado el tiempo de preguntar si se desea salir, y dentro de este bucle, utilizar una función de temporizador para esperar 3 segundos antes de continuar con la ejecución del código. Una forma de hacerlo es utilizando la librería time y la función sleep().


import random
import time

start_time = time.time()
end_time = start_time + 300  # 5 minutos en segundos
number_to_guess = random.randint(1, 10)
next_ask_time = time.time() + 10

total_hits = 0
total_misses = 0

while time.time() < end_time:
    user_guess = random.randint(1, 10)
    if user_guess == number_to_guess:
        print("¡Enhorabuena, se ha adivinado el número correcto es: ", number_to_guess)
        number_to_guess = random.randint(1, 10)
        total_hits += 1
    else:
        print("El número generado: ", user_guess,
              " no es correcto. Inténtalo de nuevo.")
        total_misses += 1
    time.sleep(2)
    if time.time() > next_ask_time:
        user_continue = input("¿Deseas salir? (S/N)")
        if user_continue.upper() == "S":
            print("¡Hasta luego! Gracias por jugar.")
            print("Aciertos: ", total_hits)
            print("No aciertos: ", total_misses)
            exit()
        elif user_continue.upper() == "N":
            next_ask_time = time.time() + 10
        else:
            time.sleep(3)
            print("No se ha ingresado una opcion valida, se continua con el juego")
            next_ask_time = time.time() + 10

print("El tiempo se ha acabado, gracias por jugar.")
print("Aciertos: ", total_hits)
print("No aciertos: ", total_misses)


# En este caso, se utiliza una función sleep(3) dentro del else, que espera 3 segundos antes de continuar con la ejecución del código y se imprime un mensaje de no se ha ingresado una opcion valida.
