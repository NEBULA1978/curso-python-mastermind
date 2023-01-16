
# Con este código se establece un bucle while dentro del if que verifica si se ha alcanzado el tiempo de preguntar si se desea salir. Dentro de este bucle, se pide al usuario que ingrese su respuesta y se verifica si es "S" o "N" mediante la función upper() que convierte el valor ingresado en mayúsculas para compararlo con las respuestas esperadas. Si la respuesta ingresada es válida, se sale del bucle y se establece el tiempo para preguntar de nuevo en 10 segundos. Si la respuesta es inválida, se muestra un mensaje de error y se sigue en el bucle hasta que se ingrese una respuesta válida.


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
        while True:
            user_continue = input("¿Deseas salir? (S/N)")
            if user_continue.upper() == "S":
                print("¡Hasta luego! Gracias por jugar.")
                exit()
            elif user_continue.upper() == "N":
                ask_time = time.time() + 10
                break
            else:
                print("Por favor ingresa S o N")
print("El tiempo se ha acabado, gracias por jugar.")
