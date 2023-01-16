# Para evitar que el programa termine cuando se presiona Enter después de 10 segundos, se puede agregar una comparación adicional dentro del if -else que verifica si la respuesta es vacía("").
# En cuanto a contar las veces que se ha acertado o fallado, se pueden crear dos variables, una para contar los aciertos y otra para contar los errores, y aumentarlas en cada iteración del bucle correspondiente.

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
    else:
        fallos += 1
        print("El número generado: ", user_guess,
              " no es correcto. Inténtalo de nuevo.")
    time.sleep(2)
    if time.time() > ask_time:
        user_continue = input("¿Deseas salir? (S/N)")
        if user_continue.upper() == "S" or user_continue == "":
            print("¡Hasta luego! Gracias por jugar.")
            break
        ask_time = time.time() + 10

print("Has acertado", aciertos, "veces y fallado", fallos, "veces")
print("El tiempo se ha acabado, gracias por jugar.")
