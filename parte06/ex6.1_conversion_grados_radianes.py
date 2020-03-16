# Ejercicio 1. Convertir grados a radianes.

from math import pi

grados = float(input('Digite los grados: '))

radianes = pi * grados / 180

print('{} grados son equivalentes a {} radianes'.format(grados, radianes))
