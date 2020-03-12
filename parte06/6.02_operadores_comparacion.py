# Operadores de comparación.

# 1. Igual: ==

programa_1 = 'Visual Studio Code'
programa_2 = 'visual studio Code'

print("¿'{}' es igual a '{}'?: {}".format(programa_1, programa_2, programa_1 == programa_2))

programa_3 = 'Visual Studio Code'
print("¿'{}' es igual a '{}'?: {}".format(programa_1, programa_3, programa_1 == programa_3))

print()

numero_1 = 1
numero_2 = 3

print("¿{} es igual a {}?: {}".format(numero_1, numero_2, numero_1 == numero_2))

numero_3 = 1
print("¿{} es igual a {}?: {}".format(numero_1, numero_3, numero_1 == numero_3))

print()

# Operador de comparación distinto: !=

numero_1 = 5
numero_2 = 7

print(f'¿{numero_1} es diferente de {numero_2}?: {numero_1 != numero_2}.')

numero_2 = 5

print(f'¿{numero_1} es diferente de {numero_2}?: {numero_1 != numero_2}.')

print()

nombre_1 = 'Daniela'
nombre_2 = 'daniela'

print(f"¿'{nombre_1}' es diferente de '{nombre_2}'?: {nombre_1 != nombre_2}")

nombre_2 = 'Daniela'
print(f"¿'{nombre_1}' es diferente de '{nombre_2}'?: {nombre_1 != nombre_2}")

print()

# Operador de comparación mayor que: >

numero_1 = 5
numero_2 = 3

resultado = numero_1 > numero_2
print('¿{} es mayor que {}?: {}'.format(numero_1, numero_2, resultado))

numero_2 = 7
resultado = numero_1 > numero_2
print('¿{} es mayor que {}?: {}'.format(numero_1, numero_2, resultado))

print()

numero_1 = 1.1
numero_2 = 1.11

resultado = numero_1 > numero_2
print('¿{} es mayor que {}?: {}'.format(numero_1, numero_2, resultado))
resultado = numero_2 > numero_1
print('¿{} es mayor que {}?: {}'.format(numero_2, numero_1, resultado))

print()

# Operador de comparación mayor o igual que: >=

numero_1 = 5
numero_2 = 5

resultado = numero_1 >= numero_2
print(f'¿{numero_1} es mayor o igual que {numero_2}?: {resultado}')

numero_1 = 3
resultado = numero_1 >= numero_2
print(f'¿{numero_1} es mayor o igual que {numero_2}?: {resultado}')

print()

numero_1 = 1.11
numero_2 = 1.1

resultado = numero_1 >= numero_2
print(f'¿{numero_1} es mayor o igual que {numero_2}?: {resultado}')

print()

# Operador de comparación menor que: <
print('Operador de comparación menor que: <')

numero_1 = 5
numero_2 = 7

resultado = numero_1 < numero_2
print(f'¿{numero_1} es menor a {numero_2}?: {resultado}')

numero_1 = 11
resultado = numero_1 < numero_2
print(f'¿{numero_1} es menor a {numero_2}?: {resultado}')

print()

numero_1 = 1.13
numero_2 = 1.17

resultado = numero_1 < numero_2
print(f'¿{numero_1} es menor a {numero_2}?: {resultado}')

numero_1 = 1.23
resultado = numero_1 < numero_2
print(f'¿{numero_1} es menor a {numero_2}?: {resultado}')

print()

# Operador de comparación menor o igual que: <=
print('Operador de comparación menor o igual que: <=')

numero_1 = 1
numero_2 = 1

resultado = numero_1 <= numero_2
print(f'¿{numero_1} es menor o igual que {numero_2}?: {resultado}')

numero_1 = 5
resultado = numero_1 <= numero_2
print(f'¿{numero_1} es menor o igual que {numero_2}?: {resultado}')

print()

numero_1 = 0.999
numero_2 = 0.9999

resultado = numero_1 <= numero_2
print(f'¿{numero_1} es menor o igual que {numero_2}?: {resultado}')

numero_1 = 1.0
resultado = numero_1 <= numero_2
print(f'¿{numero_1} es menor o igual que {numero_2}?: {resultado}')

print()

# Operador de comparación mismo objeto: is
print('Operador de comparación mismo objeto: is')

numeros_1 = [1, 2, 3, 4, 5]
numeros_2 = numeros_1
numeros_3 = [1, 2, 3, 4, 5]
numeros_4 = [1, 2, 3, 5, 4]

print(numeros_1)
print(numeros_2)
print(numeros_3)
print(numeros_4)

print()

print(numeros_1 == numeros_2)
print(numeros_1 == numeros_3)
print(numeros_2 == numeros_3)
print(numeros_1 == numeros_4)

print()

print(numeros_1 is numeros_2)
print(numeros_1 is numeros_3)
print(numeros_2 is numeros_3)

print()

# Operador de comparación distinto objeto: is not

numeros_1 = [1, 2, 3, 4, 5]
numeros_2 = numeros_1
numeros_3 = [1, 2, 3, 4, 5]
numeros_4 = [1, 2, 3, 5, 4]

print(numeros_1)
print(numeros_2)
print(numeros_3)
print(numeros_4)

print()

print(numeros_1 == numeros_2)
print(numeros_1 == numeros_3)
print(numeros_2 == numeros_3)
print(numeros_1 == numeros_4)

print()

print(numeros_1 is not numeros_2)
print(numeros_1 is not numeros_3)
print(numeros_2 is not numeros_3)
