# Números de punto flotante:

pi = 3.1415
precio = 29.95

print('El valor de la variable pi es: %.4f' % pi)
print('El valor de la variable precio es: %.2f' % precio)
print(pi)
print(precio)

print()

print('El tipo de dato para la variable pi: ', type(pi))
print('El tipo de dato para la variable precio: ', type(precio))

print()

print('Operaciones aritméticas sobre números de punto flotante:')
pi = pi * 2
print('El nuevo valor de la variable pi es:', pi)

total = precio * 5
print('El total de la compra es: %.2f' % total)

print()

print('El tipo de dato para la variable pi: ', type(pi))
print('El tipo de dato para la variable total: ', type(total))

print()

print('Creación de un número real (punto flotante) a partir de una cadena de caracteres:')

precio_computador = float(input('Digite el precio del computador: '))
print('El tipo de dato de la variable precio_computador es %s' % type(precio_computador))
print('El computador cuesta: $%.2f' % precio_computador)
