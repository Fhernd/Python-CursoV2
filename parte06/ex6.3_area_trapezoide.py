# Ejercicio 3. Calcular área de un trapezoide.

base_inferior = float(input('Escriba la base inferior (B): '))
base_superior = float(input('Escriba la base inferior (b): '))
altura = float(input('Escriba la altura (h): '))

area = (base_inferior + base_superior) / 2 * altura

print('El área del trapezoide es igual a:', area)
