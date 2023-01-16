# Aquí hay algunos ejemplos de cómo trabajar con cadenas(strings) en Python:

#     Concatenar cadenas:

x = "Hola"
y = " mundo"
result = x + y
print(result)  # imprime "Hola mundo"

# Repetir una cadena:

x = "Hola"
result = x * 3
print(result)  # imprime "HolaHolaHola"

# Acceder a un carácter específico de una cadena:

x = "Hola mundo"
result = x[4]
print(result)  # imprime "a"

# Acceder a un rango de caracteres de una cadena:

x = "Hola mundo"
result = x[4:8]
print(result)  # imprime "a mu"

# Longitud de una cadena:

x = "Hola mundo"
result = len(x)
print(result)  # imprime 10

# Reemplazar una subcadena en una cadena:

x = "Hola mundo"
result = x.replace("mundo", "Python")
print(result)  # imprime "Hola Python"

# Dividir una cadena en una lista de subcadenas:

x = "Hola mundo, bienvenido a Python"
result = x.split(",")
print(result)  # imprime ["Hola mundo", " bienvenido a Python"]

# Convertir una cadena a mayúsculas o minúsculas:

x = "Hola mundo"
result = x.upper()
print(result)  # imprime "HOLA MUNDO"

x = "HOLA MUNDO"
result = x.lower()
print(result)  # imprime "hola mundo"

# Concatenar una cadena con un formato específico:

x = "Hola"
y = " mundo"
result = "{}{}".format(x, y)
print(result)  # imprime "Hola mundo"

# Concatenar una cadena con un formato específico utilizando f-strings

x = "Hola"
y = " mundo"
result = f"{x}{y}"
print(result)  # imprime "Hola mundo"

# Hay muchas otras funciones y métodos disponibles para trabajar con cadenas en Python. Estos son solo algunos ejemplos básicos.
