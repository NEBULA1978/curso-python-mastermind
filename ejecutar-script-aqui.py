import os

# directorio donde se encuentran los archivos
directorio = '/home/next/Imágenes/Menus-bash-fusuinar/curso-python-mastermind-main'

# listar todos los archivos en el directorio
archivos = os.listdir(directorio)

# iterar sobre los archivos y ejecutarlos
for archivo in archivos:
    if archivo.endswith('.py'):  # solo ejecutar archivos con extensión .py
        while True:
            print(f'Ejecutando {archivo}...')
            resultado = os.system(f'python3 {directorio}/{archivo} 2>&1')
            if resultado != 0:
                print(f'Se produjo un error al ejecutar {archivo}:')
                print(resultado)
            
            # preguntar si el usuario desea continuar ejecutando el siguiente archivo
            respuesta = input('¿Desea continuar con el siguiente archivo? (s/n/x para salir) ')
            if respuesta.lower() == 'n':
                break
            elif respuesta.lower() == 'x':
                exit()
