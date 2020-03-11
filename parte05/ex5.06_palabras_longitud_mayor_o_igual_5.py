# Ejercicio 5.6: Encontrar las palabras de una lista que tienen al menos 5 caracteres de longitud.

paises = ['Colombia', 'Perú', 'Alemania', 'Estados Unidos', 'China', 'Argentina', 'Irán', 'Irak']

print('Contenido actual de la variable `paises`:', paises)
print('Cantidad actual de elementos de la variable `paises`:', len(paises))

print()

# Solución #1:
print('Solución #1')
paises_mas_5_caracteres = []

for p in paises:
    if len(p) >= 5:
        paises_mas_5_caracteres.append(p)

print('Contenido actual de la variable `paises_mas_5_caracteres`:', paises_mas_5_caracteres)
print('Cantidad actual de elementos de la variable `paises_mas_5_caracteres`:', len(paises_mas_5_caracteres))

print()

# Solución #2:
print('Solución #2')

paises_mas_5_caracteres = [p for p in paises if len(p) >= 5]
print('Contenido actual de la variable `paises_mas_5_caracteres`:', paises_mas_5_caracteres)
print('Cantidad actual de elementos de la variable `paises_mas_5_caracteres`:', len(paises_mas_5_caracteres))
