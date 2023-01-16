# Para que el programa te pregunte si deseas salir cada 10 segundos, se puede utilizar un contador de tiempo adicional dentro del bucle principal y una estructura de control de flujo if -else .
# Aquí te dejo un ejemplo de cómo podría ser el código modificado:


import random
import time

start_time = time.time()
end_time = start_time + 300  # 5 minutos en segundos
number_to_guess = random.randint(1, 10)
ask_time = time.time() + 10

while time.time() < end_time:
    user_guess = random.randint(1, 10)
    if user_guess == number_to_guess:
        print("¡Enhorabuena, se ha adivinado el número correcto es: ", number_to_guess)
        number_to_guess = random.randint(1, 10)
    else:
        print("El número generado: ", user_guess,
              " no es correcto. Inténtalo de nuevo.")
    time.sleep(2)
    if time.time() > ask_time:
        user_continue = input("¿Deseas salir? (S/N)")
        if user_continue.upper() == "S":
            print("¡Hasta luego! Gracias por jugar.")
            exit()
        ask_time = time.time() + 10
print("El tiempo se ha acabado, gracias por jugar.")
