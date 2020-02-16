# Números enteros:

puntaje = 300
x = -5

print(type(puntaje))
print(type(x))

print()
print('Puntaje antes de la adición 50 puntos: %i' % puntaje)
puntaje = puntaje + 50 # puntaje += 50
print('Puntaje después de la adición 50 puntos: %i' % puntaje)
print(type(puntaje))

print()

print('Valor de x antes de la adición: %i' % x)
x += 10 # x = x + 10
print('Valor de x después de la adición: %i' % x)
print('Tipo de dato de la variable `x`: %s' % type(x))

print()

print('Uso de la clase int() para crear números enteros:')

edad = int(input('Escriba su edad: '))
print('Tipo de dato de la variable edad: %s' % type(edad))

total_dias = edad * 365
print('Total de días vividos hasta el momento: %i' % total_dias)
