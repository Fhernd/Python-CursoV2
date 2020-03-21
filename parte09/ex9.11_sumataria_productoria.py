# Ejercicio 9.11: Solicitar al usuario una cantidad arbitria de valor numéricos y luego calcular su suma y productoria.

numeros = []

while True:
    cadena = input('Digite un número (o escriba "Salir" para terminar): ')

    if cadena.lower().strip() == 'salir':
        break

    numeros.append(float(cadena))


if len(numeros) > 0:
    suma = 0
    producto = 1

    for n in numeros:
        suma += n
        producto *= n

    print('Suma:', suma)
    print('Producto:', producto)
else:
    print('No hay números en la lista.')
