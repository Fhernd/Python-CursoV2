# Ejercicio 9.3: Generar los primeros 50 números de la serie Fibonacci.

# Solución:

# 0 1 1 2 3 5 8 13 21 54 85 ...

a = 0
b = 1

print(a, b, end=' ')

for i in range(48):
    a, b = b, a + b
    print(b, end=' ')
