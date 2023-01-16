import random
import time

# Inicializando variables
inicio_tiempo = time.time()
final_tiempo = inicio_tiempo + 300  # 5 minutos en segundos
numero_a_adivinar = random.randint(1, 10)
tiempo_pregunta_siguiente = time.time() + 10
aciertos_totales = 0
fallos_totales = 0

# Iniciando el bucle principal
while time.time() < final_tiempo:
    # Obteniendo la respuesta del usuario
    respuesta_usuario = random.randint(1, 10)
    if respuesta_usuario == numero_a_adivinar:
        print("¡Enhorabuena, se ha adivinado el número correcto es: ",
              numero_a_adivinar)
        numero_a_adivinar = random.randint(1, 10)
        aciertos_totales += 1
    else:
        print("El número generado: ", respuesta_usuario,
              " no es correcto. Inténtalo de nuevo.")
        fallos_totales += 1

    # Preguntando si el usuario desea salir
    if time.time() > tiempo_pregunta_siguiente:
        continuar_juego = input("¿Deseas salir? (S/N)")
        if continuar_juego.upper() == "S":
            print("¡Hasta luego! Gracias por jugar.")
            print("Aciertos: ", aciertos_totales)
            print("Fallos: ", fallos_totales)
            exit()
        elif continuar_juego.upper() == "N":
            tiempo_pregunta_siguiente = time.time() + 10
        else:
            tiempo_inicio_respuesta_usuario = time.time()
            while (time.time() - tiempo_inicio_respuesta_usuario) < 3:
                continuar_juego = input("¿Deseas salir? (S/N)")
                if continuar_juego.upper() == "S":
                    print("¡Hasta luego! Gracias por jugar.")
                    print("Aciertos: ", aciertos_totales)
                    print("Fallos: ", fallos_totales)
                    exit()
                elif continuar_juego.upper() == "N":
                    tiempo_pregunta_siguiente = time.time() + 10
                    break
            else:
                print("No se ha ingresado una opcion valida, se continua con el juego")
                tiempo_pregunta_siguiente = time.time() + 10

# Mostrando resultados finales
print("El tiempo se ha acabado, gracias por jugar.")
print("Aciertos: ", aciertos_totales)
print("Fallos: ", fallos_totales)
