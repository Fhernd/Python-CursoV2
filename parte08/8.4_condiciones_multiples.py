# Evaluación de múltiples condiciones en una cláusula (sentencia) if:

numero = int(input('Escriba un número entero: '))

if numero % 5 == 0 and numero >= 20 and numero <= 40:
    print('El número {} es divisible entre 5 y se halla en el rango 20 a 40.'.format(numero))
else:
    print('El número {} no es divisible entre 5 y no se halla en el rango 20 a 40.'.format(numero))
