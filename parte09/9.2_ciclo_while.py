import random

# Ciclo while

numeros = [1, 2, 3, 4, 5]

i = 0

while i < len(numeros):
    print(numeros[i])
    i += 1

print()

print('Contenido de la lista `numeros`:', numeros)

print()

# Suma de los elementos de una lista con un ciclo while:
print('Suma de los elementos de una lista con un ciclo while:')

i = 0
total = 0

while i < len(numeros):
    total += numeros[i]
    i += 1

print('Suma de los números de 1 a 5:', total)

print()

numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)

print('Contenido de la lista `numeros`:', numeros)

print()

# Suma de los valores pares en la lista `numeros`:

suma_pares = 0
i = 0

while i < len(numeros):
    if numeros[i] % 2 == 0:
        suma_pares += numeros[i]
    i += 1

print('Suma de todos los valores pares que hay en el rango 1-10:', suma_pares)

print()

# Suma de los valores impares que hay en la lista `numeros`:

suma_impares = 0
i = 0

while i < len(numeros):

    if numeros[i] % 2 != 0:
        suma_impares += numeros[i]

    i += 1

print('Suma de los valores impares en el rango 1 a 10:', suma_impares)

print()

# Terminación arbitraria de la ejecución de un ciclo while:
print('Terminación arbitraria de la ejecución de un ciclo while:')

total = 0

while True:
    numero = int(input('Escriba un número entero positivo (un número igual o menor a cero para terminar): '))

    if numero <= 0:
        break
    
    total += numero

print('El acumulado en total es igual a', total)

print()

# Adivinar un número - Máximo tres intentos.

numero_aleatorio = random.randint(1, 15)
intentos_restantes = 3

while intentos_restantes > 0:
    numero = int(input('Adivine un número entre 1 y 15: '))

    if numero == numero_aleatorio:
        break
    else:
        print()
        print('No has digitado el número correcto.')
    
    intentos_restantes -= 1

if intentos_restantes != 0:
    print('¡Génial! ¡Has ganado!')
else:
    print('¡Perdiste! ¡Sigue intentándolo!')
