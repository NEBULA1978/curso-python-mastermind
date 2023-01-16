# ¡De Libras a Euros!: Diseña un programa que realice el cambio de libras a euros. Primero debe preguntar la cantidad de libras que queremos cambiar y después, el valor de la conversión

libras = float(input("Ingrese la cantidad de libras que desea cambiar: "))
tipo_cambio = float(
    input("Ingrese el valor de la conversión (libras a euros): "))
euros = libras * tipo_cambio
print("{} libras son {:.2f} euros.".format(libras, euros))


# En este programa se pide al usuario que ingrese la cantidad de libras que desea cambiar utilizando el método input(). También se pide el valor de la conversión, también con input(). Luego, se multiplica la cantidad de libras por el valor de conversión para obtener la cantidad en euros y se almacena en la variable euros. Por último, se utiliza el método format() para imprimir el resultado de la conversión en una cadena legible para el usuario.

# Es importante
