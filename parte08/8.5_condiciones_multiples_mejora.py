# Mejora evaluación de múltiples condiciones en una cláusula (sentencia) if:

numero = int(input('Escriba un número entero: '))

# numero >= 20 and numero <= 40
# a <= x <= b

# 20 <= numero <= 40

if numero % 5 == 0 and 20 <= numero <= 40:
    print('El número {} es divisible entre 5 y se halla en el rango 20 a 40.'.format(numero))
else:
    print('El número {} no es divisible entre 5 y no se halla en el rango 20 a 40.'.format(numero))
