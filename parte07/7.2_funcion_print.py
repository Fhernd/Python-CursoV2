# Salida de datos (output) - Función incorporada `print()`:

nombre = 'John Ortiz Ordoñez'
edad = 29

print('Nombre: ' + nombre, end=' - ')
print('Edad: ' + str(edad))

print()

print('Aprendiendo el uso de la', end=' ')
print('función print()')

print()

# Múltiples argumentos para la función `print()`:
print('Múltiples argumentos para la función `print()`:')

email = 'john@mail.co'

print(nombre, edad, email)

print(nombre, edad, email, sep='')
print(nombre, edad, email, sep=' - ')

print()

lenguajes = ('Python', 'JavaScript', 'C++', 'C#', 'Java')

print(lenguajes)
print(lenguajes[0], lenguajes[1], lenguajes[2], lenguajes[3], lenguajes[4], sep=' - ')

print()

# Expansión (desempaquetamiento) de una colección:
print(*lenguajes, sep=' - ')
