# Ejercicio 5.11: Encontrar los tres valores mayores en un diccionario.

from heapq import nlargest

productos = {'Mouse': 29.9, 'Teclado': 119.9, 'Audífonos': 35.9, 'Monitor': 299}

productos_mas_caros_3 = nlargest(3, productos, key=productos.get)

print('Los tres productos más caros son:', productos_mas_caros_3)
