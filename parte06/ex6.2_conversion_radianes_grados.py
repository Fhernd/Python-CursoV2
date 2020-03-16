# Ejercicio 2. Convertir radianes a grados.

from math import pi

radianes = float(input('Digite los grados: '))

grados = 180 * radianes / pi

print('{} radianes equivalen a {} grados'.format(radianes, grados))
