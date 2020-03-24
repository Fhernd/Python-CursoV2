# Gestión de excepciones en operaciones aritméticas - división:
print('Gestión de excepciones en operaciones aritméticas - división:')

# Captura del primero número - dividendo:

while True:
    try:
        dividendo = float(input('Escriba el dividendo: '))

        break
    except:
        print('MENSAJE: Debe escribir un valor válido. Intente de nuevo.')
    print()

print()

while True:
    try:
        divisor = float(input('Escriba el divisor: '))

        break
    except:
        print('MENSAJE: Debe escribir un valor válido. Intente de nuevo.')
    print()

try:
    division = dividendo / divisor

    print('El resultado de la división es:', division)
except ZeroDivisionError as e:
    print('ERROR:', e)
    print('MENSAJE: Intento de división entre cero.')
