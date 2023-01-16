# Para solucionar esto, se puede agregar una variable booleana is_equal para indicar si los números son iguales y sólo imprimir el mensaje una vez.

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

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
if is_equal:
    print("Los números ingresados son iguales.")

for i in range(len(nums)):
    print(f"El número en la posición {i+1} es: {nums[i]}")
