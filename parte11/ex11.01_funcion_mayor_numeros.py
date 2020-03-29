# Ejercicio 11.1: Crear una función para obtener el mayor de tres números.

# a, b, c

def numero_mayor(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return None

x = 3
y = 2
z = 0

mayor = numero_mayor(x, y, z)
print(f'El número mayor entre {x}, {y}, y {z} es {mayor}')

print()

x = 3
y = 3
z = 3

mayor = numero_mayor(x, y, z)
if mayor:
    print(f'El número mayor entre {x}, {y}, y {z} es {mayor}')
else:
    print('Los tres números son iguales. Ninguno es mayor.')
