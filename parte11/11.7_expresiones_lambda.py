# Expresiones lambda - Funciones anónimas
print('Expresiones lambda - Funciones anónimas')

def sumar(a, b):
    resultado = a + b
    return resultado

x = 2
y = 3

print('La suma de {} + {} es igual a {}'.format(x, y, sumar(x, y)))

print()

sumar_lambda = lambda a, b: a + b
print('La suma de {} + {} es igual a {}'.format(x, y, sumar_lambda(x, y)))
