while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num3 = int(input("Ingrese el tercer número: "))
        break
    except ValueError:
        print("Por favor ingrese un número válido.")

nums = [num1, num2, num3]
is_equal = num1 == num2 == num3

if is_equal:
    print("Los números ingresados son iguales.")
else:
    print("El número más pequeño es:", min(nums))
    print("El número más grande es:", max(nums))


# Sí, en lugar de utilizar ciclos for para encontrar el número más grande y más pequeño, se pueden usar las funciones max() y min() de Python.
