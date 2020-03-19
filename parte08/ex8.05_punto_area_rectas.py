# Ejercicio 8.5. Dadas las rectas y = 2x - 2, y = x + 1, x = 10 comprobar si un punto está en el área comprendida entre las rectas.

x = float(input('Escriba el valor de x: '))
y = float(input('Escriba el valor de y: '))

if x <= 10:
    valor_1 = 2 * x - 2
    valor_2 = x + 1

    if valor_2 <= y <= valor_1:
        print('El punto ({}, {}) se halla en el área de las tres rectas.'.format(x, y))
    else:
        print('El punto ({}, {}) no se halla en el área de las tres rectas.'.format(x, y))
else:
    print('El punto ({}, {}) no se halla en el área de las tres rectas.'.format(x, y)) 
