# Linealización de expresiones algebraicas a expresiones programáticas.

# Ejemplo 1. Linealizar ecuación cuadrática.

a = 1
b = 0
c = -1

x_1 = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
x_2 = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)

print('Solución 1 (x_1):', x_1)
print('Solución 1 (x_2):', x_2)
