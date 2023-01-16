# Ejemplo de cómo hacerlo utilizando el método round():

fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("{} grados Fahrenheit son {:.2f} grados Celsius.".format(
    fahrenheit, round(celsius, 2)))
