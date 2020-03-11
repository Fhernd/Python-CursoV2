# Ejercicio 5.12: Convertir un diccionario en su representación en el formato JSON.

import json

productos = {'Mouse': 29.9, 'Teclado': 119.9, 'Audífonos': 35.9, 'Monitor': 299}

print('Contenido actual del diccionario `productos`:', productos)
print('El tipo de dato de la variable `productos` es:', type(productos).__name__)

print()

productos_json = json.dumps(productos)
print('Contenido actual de la variable `productos_json`:', productos_json)
print('El tipo de dato de la variable `productos_json` es:', type(productos_json).__name__)
