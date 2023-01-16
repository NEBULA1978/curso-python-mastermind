# Para verificar si se ingresaron dos o tres números iguales, se puede utilizar un conjunto para almacenar los números ingresados y comparar su tamaño con el número de números ingresados. Si el tamaño del conjunto es menor que el número de números ingresados, significa que hay números repetidos.
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
nums.sort()

unique_nums = set(nums)
if len(unique_nums) < len(nums):
    print("Hay números repetidos.")
else:
    print("El número más pequeño es:", nums[0])
    print("El número más grande es:", nums[-1])
