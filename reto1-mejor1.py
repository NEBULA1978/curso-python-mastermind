# Para imprimir el orden de los números ingresados y su valor, se pueden usar dos ciclos for anidados. El primero para recorrer los números ingresados y el segundo para comparar cada número con los demás.

# Por ejemplo:

while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num3 = int(input("Ingrese el tercer número: "))
        break
    except ValueError:
        print("Por favor ingrese un número válido.")

nums = [num1, num2, num3]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        elif (num1 == num2 == num3):
            print("Los números ingresados son iguales.")

for i in range(len(nums)):
    print(f"El número en la posición {i+1} es: {nums[i]}")


# En este ejemplo se utiliza el método de ordenamiento "Bubble Sort" para ordenar los números de menor a mayor y luego se imprime cada uno junto con su posición en la lista.

# El problema es que el mensaje "Los números ingresados son iguales" se está imprimiendo en cada iteración del ciclo for anidado, debido a que el condicional if (num1 == num2 == num3): se encuentra dentro del ciclo for anidado.

# Para solucionar esto, se puede agregar una variable booleana is_equal para indicar si los números son iguales y sólo imprimir el mensaje una vez.
