# Tipo de dato compuesto: lista
# Las listas son un tipo de dato dinámico

# 1. Creación de una lista:
numeros = [2, 4, 6, 8, 10]
print('Tipo de dato de la variable numeros:', type(numeros))
print('Cantidad de elementos:', len(numeros))
print('Contenido:', numeros)

print()

# 2. Acceso a los elementos de una lista:
dos = numeros[0]
print('El primer elemento (índice 0) de la lista es:', dos)
diez = numeros[4]
print('El último elemento (índice 4) de la lista es:', diez)

diez = numeros[-1]
print('El último elemento (índice -1) de la lista es:', diez)

print()

subseccion = numeros[1:4]
print('Tipo de dato de la variable subseccion:', type(subseccion))
print('Cantidad de elementos:', len(subseccion))
print('Contenido:', subseccion)

print()

# Acceso con desempaquetamiento:
print('Acceso a datos de una lista con desempaquetamiento:')
cuatro, seis, ocho = subseccion
print(cuatro, seis, ocho)

print()

# 2. Modificación de una lista:
print('2. Modificación de elementos de una lista:')
print('El primer elemento (índice 0) de la lista es:', numeros[0])
numeros[0] = 1
print('El primer elemento (índice 0) de la lista es:', numeros[0])
