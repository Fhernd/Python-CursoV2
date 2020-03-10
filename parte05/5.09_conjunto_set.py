# Tipo de dato compuesto mutable y dinámico: set (conjunto)

# 1. Creación de un conjunto:
print('1. Creación de un conjunto:')

conjunto_1 = {'Juan', 'Oliva', 'Edward', 'Daniela', 'Juan', 'Juan', 'Germán'}
conjunto_2 = set(['Juan', 'Oliva', 'Edward', 'Daniela', 'Juan', 'Juan', 'Germán'])

print('Contenido de la variable `conjunto_1`:', conjunto_1)
print('Cantidad de elementos del conjunto `conjunto_1`:', len(conjunto_1))
print('El tipo de dato de la variable `conjunto_1` es:', type(conjunto_1))
print()
print('Contenido de la variable `conjunto_2`:', conjunto_2)
print('Cantidad de elementos del conjunto `conjunto_2`:', len(conjunto_2))
print('El tipo de dato de la variable `conjunto_2` es:', type(conjunto_2))

print()

# 1.2 Creación de conjuntos por medio de cadenas de caracteres:
print('1.2 Creación de conjuntos por medio de cadenas de caracteres:')
frase = 'Python es un lenguaje de programación'
caracteres = set(frase)
print('Contenido de la variable conjunto `caracteres`:', caracteres)
print('El tipo de dato de la variable `caracteres` es:', type(caracteres))
print('Cantidad de elementos del conjunto `caracteres`:', len(caracteres))
print('Cantidad de caracteres de la variable string `frase`:', len(frase))
