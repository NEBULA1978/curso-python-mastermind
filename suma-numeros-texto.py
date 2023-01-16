# En Python, no es posible sumar números y textos(cadenas) directamente. Si intenta sumar un número y una cadena, obtendrá un error de tipo "TypeError".

# Por ejemplo, si intenta sumar el número 3 con la cadena "hola", obtendrá un error:


num = 3
text = "hola"
result = num + text
print(result)
# Error
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

num = 3
text = "hola"
result = str(num) + text
print(result)

# Resultado= 3hola

# Otra forma es utilizando f-strings

num = 3
text = "hola"
result = f"{num} {text}"
print(result)  # 3 hola

# De esta manera se puede concatenar un número y una cadena, pero no sumarlos.


# En lugar de utilizar la concatenación de cadenas o f-strings, también se puede utilizar el método format() para insertar el valor del número en una cadena.

# Por ejemplo:
num = 3
text = "hola"
result = "{} {}".format(num, text)
print(result)

# En este caso, el método format() reemplaza los placeholders {} en la cadena con los valores dados. El primer placeholder {} es reemplazado con el valor de la variable num y el segundo placeholder {} es reemplazado con el valor de la variable text.

# El resultado es el mismo que en el ejemplo anterior "3 hola"

# Nota: El método format es compatible con versiones anteriores de python y es una forma mas legible de concatenar variables.
