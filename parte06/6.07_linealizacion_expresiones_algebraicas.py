import math

# Linealización de expresiones algebraicas a expresiones programáticas.

# Ejemplo 1. Linealizar ecuación cuadrática.

a = 1
b = 0
c = -1

x_1 = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
x_2 = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)

print('Solución 1 (x_1):', x_1)
print('Solución 1 (x_2):', x_2)

print()

# Ejemplo 2. X^2 + 4YZ

x = 1
y = 2
z = 3

resultado = x**2 + 4*y*z
print('Resultado:', resultado)

print()

# Ejemplo 3. 

resultado = (x + y)/z + 3*x/5 + 4*y
print('Resultado:', resultado)

print()

# Ejemplo 4.

c = 5
d = 3

resultado = (4*x**2 - 2*x + 8) / (c - d)
print('Resultado:', resultado)

# Ejemplo 5.

resultado = 4/3 * math.pi
print('Resultado:', resultado)
