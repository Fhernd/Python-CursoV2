# Números complejos:

numero_complejo = 2 - 3j
print('Contenido variable compleja:', numero_complejo)
print('El tipo de dato de la variable numero_complejo es:', type(numero_complejo))

print()

numero_complejo = complex(2, -3)
print('Contenido variable compleja:', numero_complejo)
print('El tipo de dato de la variable numero_complejo es:', type(numero_complejo))

print()

print('Operaciones aritméticas sobre números complejos:')

suma = 2 - 3j + (1 + 5j)
print('Suma:', suma)

resta = 2 - 3j - complex(1, 5)
print('Resta:', resta)

producto = 2 - 3j * complex(1, 5)
print('Producto:', producto)

division = 2 - 3j / complex(1, 5)
print('División:', division)
