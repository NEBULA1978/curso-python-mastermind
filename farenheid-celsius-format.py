# Ejemplo de cómo hacerlo utilizando el método round():

fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("{} grados Fahrenheit son {:.2f} grados Celsius.".format(fahrenheit, celsius))


# En ambos casos se utiliza el formato {: .2f} dentro de la cadena de formato para indicar que se desea mostrar sólo dos decimales en la salida.
# En el primer caso se utiliza el método round para redondear el valor de la variable celsius a dos decimales antes de insertarlo en la cadena.
# En el segundo caso se utiliza directamente la variable celsius con el formato especificado.
