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

        if edad > 0:
            if edad <= 70:
                break
            else:
                print('MENSAJE: La edad no debe superar los 70 años.')
        else:
            print('MENSAJE: El valor para la edad debe ser un número positivo.')
    except:
        print('MENSAJE: No ha escrito un valor válido. Intente de nuevo.')
    
    print()

print('Su edad es:', edad, 'años.')
