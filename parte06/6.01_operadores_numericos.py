import math

# Operadores numéricos:

# Operador suma: +

numero_1 = 2
numero_2 = 3

suma = numero_1 + numero_2

print(f'La suma de {numero_1} y {numero_2} es igual a {suma}')

print()

suma = 2 + 3
print(f'La suma de {2} y {3} es igual a {suma}')

print()

suma = numero_1 + 3
print(f'La suma de {numero_1} y {3} es igual a {suma}')

print()
# Suma de n cantidad de elementos:
print('Suma de n cantidad de elementos:')
suma = 1 + 2 + 3 + 4 + 5
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15

print('La suma de los números de 1 a 5 es igual a:', suma)

print()

# Suma de números reales (punto flotante):
print('Suma de números reales (punto flotante):')
numero_1 = 3.1415
numero_2 = 2.7172

suma = numero_1 + numero_2
print(f'La suma de {numero_1} y {numero_2} es igual {suma}.')

print()

print('Suma de números reales como literales:')

suma = 3.1415 + 2.7172
print(f'La suma de {3.1415} y {2.7172} es igual {suma}.')

print()

print('Suma de valores de punto flotante como variable y literal:')

suma = numero_1 + 2.7172
print(f'La suma de {numero_1} y {2.7172} es igual {suma}.')

print()

# Suma de múltiples valores de punto flotante en una única instrucción:
print('Suma de múltiples valores de punto flotante en una única instrucción:')

suma = 1.1 + 2.2 + 3.3 + 4.4 + 5.5
# 1.1 + 2.2 = 3.3
# 3.3 + 3.3 = 6.6
# 6.6 + 4.4 = 11.0
# 11.0 + 5.5 = 16.5
print('La suma de 1.1 + 2.2 + 3.3 + 4.4 + 5.5 es igual a', suma)

print()

# Operador resta: -
print('Operador resta: -')
numero_1 = 5
numero_2 = 3

resta = numero_1 - numero_2 # 5 - 3

print(f'La resta de {numero_1} y {numero_2} es igual {resta}.')

print()

print('Resta de valores enteros literales:')

resta = 5 - 3
print(f'La resta de {5} y {3} es igual {resta}.')

print()

print('Resta de una variable y una literal:')

resta = numero_1 - 3
print(f'La resta de {numero_1} y {3} es igual {resta}.')

print()

print('Expresión de resta con múltiples valores:')

resta = 5 - 3 - 2 - 4 - 1

# 5 - 3 = 2
# 2 - 2 = 0
# 0 - 4 = -4
# -4 - 1 = -5
print('5 - 3 - 2 - 4 - 1 es igual a', resta)

print()

# Resta de valores numéricos reales (punto flotante):
print('Resta de valores numéricos reales (punto flotante):')

numero_1 = 3.1415
numero_2 = 2.7172

resta = numero_1 - numero_2
print(f'La resta de {numero_1} y {numero_2} es igual {resta}.')

print()

print('Resta de valores numéricos reales como literales:')

resta = 3.1415 - 2.7172
print(f'La resta de {3.1415} y {2.7172} es igual {resta}.')

print()

print('Resta de una variable numérica real y una literal numérica real:')

resta = numero_1 - 2.7172
print(f'La resta de {numero_1} y {2.7172} es igual {resta}.')

print()

# Invertir el signo de una literal numérica (entera o real) con el operador de resta (-):
print('Invertir el signo de una literal numérica (entera o real) con el operador de resta (-):')

numero = 100

print('El valor de la variable `numero` es igual a', numero)
print('El valor de la variable `numero` es igual a', -numero)
print('El valor de la variable `numero` es igual a', numero)

print()

numero = -100
print('El valor de la variable `numero` es igual a', numero)
print('El valor de la variable `numero` es igual a', -numero)
print('El valor de la variable `numero` es igual a', numero)

print()

pi = math.pi

print('El valor de la variable `pi` es igual a', pi)
print('El valor de la variable `pi` es igual a', -pi)

print()

# Operador producto (multiplicación): *
print('Operador producto (multiplicación): *')

numero_1 = 3
numero_2 = 7

producto = numero_1 * numero_2
print(f'El producto de {numero_1} por {numero_2} es igual a {producto}.')

print()

print('Producto de dos literales:')

producto = 3 * 7
print(f'El producto de {3} por {7} es igual a {producto}.')

print()

print('Producto de una variable por una literal:')

producto = numero_1 * 7
print(f'El producto de {numero_1} por {7} es igual a {producto}.')

print()

print('Producto de varios operandos:')

producto = 1 * 2 * 3 * 4 * 5

# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120

# 5! = 120

print('1 * 2 * 3 * 4 * 5 es igual a', producto)

print()

# Producto de variables o literales numéricas reales (punto flotante):
print('Producto de variables o literales numéricas reales (punto flotante):')

numero_1 = 1.1
numero_2 = 3.5

producto = numero_1 * numero_2
print(f'El producto de {numero_1} y {numero_2} es igual a {producto}.')

print()

producto = 1.1 * 3.5
print(f'El producto de {1.1} y {3.5} es igual a {producto}.')

print()

producto = numero_1 * 3.5
print(f'El producto de {numero_1} y {3.5} es igual a {producto}.')

print()

print('Producto entre varios operandos:')

producto = 1.1 * 2.2 * 3.3 * 4.4 * 5.5

print('El resultado de la operación 1.1 * 2.2 * 3.3 * 4.4 * 5.5 es igual a', producto)

print()

# Operador de división (decimales): /
print('Operador de división (decimales): /')

numero_1 = 1
numero_2 = 2

division = numero_1 / numero_2
print('La división de {} entre {} es igual a {}.'.format(numero_1, numero_2, division))

print()

print('División entre dos literales numéricas enteras:')

division = 1 / 2
print('La división de {} entre {} es igual a {}.'.format(1, 2, division))

print()

print('División entre una variable y una literal entera:')

division = numero_1 / 2
print('La división de {} entre {} es igual a {}.'.format(numero_1, 2, division))

print()

print('Expresión de división con múltiples operandos:')

division = 8 / 4 / 3 / 2

print('La expresión `8 / 4 / 3 / 2` es igual a', division)

print()

# División entre variables y literales numéricas reales (punto flotante):

print('División entre variables y literales numéricas reales (punto flotante):')

numero_1 = 0.5
numero_2 = 1.73

division = numero_1 / numero_2
print('La división de {} y {} es igual a {}.'.format(numero_1, numero_2, division))

print()

print('División de una variable y literal de punto flotante:')

division = numero_1 / 1.73
print('La división de {} y {} es igual a {}.'.format(numero_1, 1.73, division))

print()

print('División de literales de punto flotante (reales):')

division = 0.5 / 1.73
print('La división de {} y {} es igual a {}.'.format(0.5, 1.73, division))

print()

print('Múltiples diviones en una expresión:')

division = 0.5 / 1.73 / 4.5 / 7.0
print('La operación `0.5 / 1.73 / 4.5 / 7.0` es igual a:', division)

print()

# División entre cero:
print('División entre cero:')

numero_1 = 5
numero_2 = 0


print('Solución #1:')

if numero_2 != 0:
    division = numero_1 / numero_2
    print('La división de {} y {} es igual a {}.'.format(numero_1, numero_2, division))
else:
    print('MENSAJE: La división entre cero no está permitida.')

print()

print('Solución #2:')

try:
    division = numero_1 / numero_2
    print('La división de {} y {} es igual a {}.'.format(numero_1, numero_2, division))
except ZeroDivisionError as e:
    print('Error:', e)

print()

# Operador resto (residuo, módulo): %

# 5 // 2 = 2
# 5 % 2 = 1

numero_1 = 5
numero_2 = 2

division = numero_1 // numero_2
resto = numero_1 % numero_2

print(f'La división entera de {numero_1} y {numero_2} es igual a {division}.')
print(f'El resto de la división entera de {numero_1} y {numero_2} es igual a {resto}.')

print()

print('¿Es número par o impar?')

if numero_1 % 2 == 0:
    print('El valor {} es par.'.format(numero_1))
else:
    print('El valor {} es impar.'.format(numero_1))

print()

# Operador de división entera: //

numero_1 = 5
numero_2 = 2

division = numero_1 / numero_2

print(f'División entre {numero_1} y {numero_2} es igual a {division}.')

print()

division_entero = numero_1 // numero_2
print(f'División entera entre {numero_1} y {numero_2} es igual a {division_entero}.')

print()

# Operador de potencia: **
print('Operador de potencia: **')

base = 2
exponente = 3

potencia = base ** exponente

print(f'La potencia de {base}^{exponente} es igual a {potencia}.')

print()

potencia = pow(base, exponente)
print(f'La potencia de {base}^{exponente} es igual a {potencia}.')
