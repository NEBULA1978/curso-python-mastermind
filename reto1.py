# Un ejemplo de código en Python3 en el que el usuario puede introducir 3
# números y el programa devuelve el número más pequeño y el más grande:

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

nums = [num1, num2, num3]
nums.sort()

print("El número más pequeño es:", nums[0])
print("El número más grande es:", nums[-1])


# En primer lugar, se asigna un valor entero
# a cada variable num1, num2 y num3 utilizando
# la función input() para recibir la entrada del
# usuario. Luego, se crea una lista llamada nums
# que contiene los tres números. Utilizando el
# método sort() se ordenan de menor a mayor y
# se imprime el primer valor de la lista (mas pequeño)
# y el ultimo valor (mas grande)

# Es importante que el usuario ingrese solo numeros
# y no caracteres para evitar errores en el programa.


# como se puede evitar el error sino ingresa numeros

# Para evitar errores en el programa si el usuario no ingresa números, se puede utilizar una estructura de control de excepciones en Python. La estructura try -except permite intentar ejecutar un bloque de código y, en caso de que ocurra un error, ejecutar un bloque de código específico.

# Aquí te muestro un ejemplo de cómo se puede utilizar try -except para evitar errores si el usuario no ingresa números:

while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num3 = int(input("Ingrese el tercer número: "))
        break
    except ValueError:
        print("Por favor ingrese un número válido.")

nums = [num1, num2, num3]
nums.sort()

print("El número más pequeño es:", nums[0])
print("El número más grande es:", nums[-1])


# En este caso se utiliza un ciclo while que se ejecutara siempre, dentro de el se encuentra el bloque try que contiene las instrucciones para solicitar los tres numeros al usuario, si el usuario ingresa un valor
