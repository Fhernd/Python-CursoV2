# Entrada de datos (input) - Función incorporada `input()`:

print('Entrada de datos (input) - Función incorporada `input()`:')

try:
    nombre = input('Digite su nombre: ')

    print('El tipo de dato de la variable `nombre` es:', type(nombre).__name__)
    print('El contenido de la variable `nombre` es:', nombre)
except EOFError:
    print('El usuario ha cancelado la introducción de datos.')
    print('El nombre de la persona no se capturó.')

print('El programa ha finalizado de forma satisfactoria.')
