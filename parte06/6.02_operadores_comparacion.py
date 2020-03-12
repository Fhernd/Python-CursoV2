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
