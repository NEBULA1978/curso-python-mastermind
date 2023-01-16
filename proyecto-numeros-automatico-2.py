# Claro, se pueden dar nombres más descriptivos a las variables para hacer el código más legible y fácil de entender. Por ejemplo, en lugar de usar las variables start_time, end_time, number_to_guess, ask_time, user_guess, hits y miss, se pueden utilizar nombres más descriptivos como start_time, end_time, number_to_guess, next_ask_time, user_guess,


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
        while True:
            user_continue = input("¿Deseas salir? (S/N)")
            if user_continue.upper() == "S":
                print("¡Hasta luego! Gracias por jugar.")
                print("Aciertos: ", total_hits)
                print("No aciertos: ", total_misses)
                exit()
            elif user_continue.upper() == "N":
                next_ask_time = time.time() + 10
                break
            else:
                print("Por favor ingresa S o N")
print("El tiempo se ha acabado, gracias por jugar.")
print("Aciertos: ", total_hits)
print("No aciertos: ", total_misses)
