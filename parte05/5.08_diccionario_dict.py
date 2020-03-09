# Tipo de dato compuesto: diccionario

# 1. Creación de diccionarios:
diccionario_1 = {'propiedad1': 1, 'propiedad2': 2, 'propiedad3': [1, 2, 3]}
diccionario_2 = dict()
diccionario_2['propiedad1'] = 1
diccionario_2['propiedad2'] = 2
diccionario_2['propiedad3'] = [1, 2, 3]

print(diccionario_1)
print(type(diccionario_1))
print()
print(diccionario_2)
print(type(diccionario_2))

print()

computador = {'id': 1001, 'marca': 'MSi', 'ram': 128, 'cpu': 'Intel Core i7 Extreme Edition', 'almacenamiento': 8}
print(computador)
print(f'La variable diccionario `computador` tiene {len(computador)} propiedades.')
print('El tipo de dato de la variable `computador` es: %s' % type(computador).__name__)
