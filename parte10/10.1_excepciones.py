# Excepciones en flujo de ejecución de un programa Python.

try:
    numero = int(input('Escriba un número entero: '))

    print('Contenido de la variable `numero`:', numero)
    print('El tipo de dato de la variable `numero` es:', type(numero))
except ValueError as e:
    print('ERROR: ', e)

print()
print('El programa ha terminado')

print()

# Captura segura de un número entero:
print('Captura segura de un número entero:')

while True:
    try:
        edad = int(input('Escribe su edad: '))

        break
    except:
        print('MENSAJE: No ha escrito un valor válido. Intente de nuevo.')

print('Su edad es:', edad)
