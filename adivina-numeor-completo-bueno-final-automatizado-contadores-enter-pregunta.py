# Para evitar que el programa termine cuando se presiona Enter después de 10 segundos, se puede agregar una comparación adicional dentro del if -else que verifica si la respuesta es vacía("").
# Adicionalmente se puede agregar un mensaje de opción incorrecta cuando se presiona Enter, seguido de una nueva pregunta para salir.

# Aquí te dejo un ejemplo de cómo podría ser el código modificado:


# import random
# import time

# start_time = time.time()
# end_time = start_time + 300  # 5 minutos en segundos
# number_to_guess = random.randint(1, 10)
# ask_time = time.time() + 10
# aciertos = 0
# fallos = 0

# while time.time() < end_time:
#     user_guess = random.randint(1, 10)
#     if user_guess == number_to_guess:
#         aciertos += 1
#         print("¡Enhorabuena, se ha adivinado el número correcto es: ", number_to_guess)
#         number_to_guess = random.randint(1, 10)
#     else:
#         fallos += 1
#         print("El número generado: ", user_guess,
#               " no es correcto. Inténtalo de nuevo.")
#     time.sleep(2)
#     if time.time() > ask_time:
#         user_continue = input("¿Deseas salir? (S/N)")
#         if user_continue.upper() == "S":
#             print("¡Hasta luego! Gracias por jugar.")
#             break
#         elif user_continue == "":
#             print("Opción incorrecta, por favor introduce S o N")
#         else:
#             ask_time = time.time() + 10

# print("Has acertado", aciertos, "veces y fallado", fallos, "veces.")
# Ramonet Pascualet
# despues de 10 segundos si pulso intro me muestra el numero tambien,para corregir?


# Para evitar que el programa muestre el número adivinado al presionar Enter después de 10 segundos, se puede agregar una nueva condición dentro del while para verificar si el número generado es igual al número a adivinar solo si se ha ingresado una respuesta válida(S o N) para la pregunta de salida.

# Aquí te dejo un ejemplo de cómo podría ser el código modificado:

import random
import time

start_time = time.time()
end_time = start_time + 300  # 5 minutos en segundos
number_to_guess = random.randint(1, 10)
ask_time = time.time() + 10
aciertos = 0
fallos = 0

while time.time() < end_time:
    user_guess = random.randint(1, 10)
    if user_guess == number_to_guess:
        aciertos += 1
        print("¡Enhorabuena, se ha adivinado el número correcto es: ", number_to_guess)
        number_to_guess = random.randint(1, 10)
    time.sleep(2)
    if time.time() > ask_time:
        user_continue = input("¿Deseas salir? (S/N)")
        if user_continue.upper() == "S":
            print("¡Hasta luego! Gracias por jugar.")
            break
        elif user_continue == "":
            print("Opción incorrecta, por favor introduce S o N")
        else:
            fallos += 1
            ask_time = time.time() + 10

print("Has acertado", aciertos, "veces y fallado", fallos, "veces.")
