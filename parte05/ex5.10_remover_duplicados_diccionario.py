# Ejercicio 5.10: Remover todos los elementos duplicados de un diccionario.

productos = {1001: 'Mouse', 1002: 'Teclado', 1003: 'Monitor', 1004: 'Mouse', 1005: 'Audífonos', 1006: 'Teclado'}

print('Contenido actual del diccionario `productos`:', productos)
print('Cantidad actual de elementos del diccionario `productos`:', len(productos))

print()

productos_unicos = {}

for k, v in productos.items():
    if v not in productos_unicos.values():
        productos_unicos[k] = v

print('Contenido actual del diccionario `productos_unicos`:', productos_unicos)
print('Cantidad actual de elementos del diccionario `productos_unicos`:', len(productos_unicos))
