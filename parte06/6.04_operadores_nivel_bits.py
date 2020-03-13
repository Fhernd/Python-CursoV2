# Operadores a nivel de bits (bitwise):
print('Operadores a nivel de bits:')

# Operador and: &
print('Operador and: &')

numero_1 = 5 # 101
numero_2 = 2 # 10

# 101
# 010 &
# ====
# 000

resultado = numero_1 & numero_2

print('numero_1 & numero_2 =', resultado)

print()

# Operador a nivel de bits (bitwise) or: |
print('Operador a nivel de bits (bitwise) or: |')

numero_1 = 5 # 101
numero_2 = 2 # 10

# 101
# 010 |
# === 
# 111

# 111 [2] = 7 [10]

resultado = numero_1 | numero_2

print('numero_1 | numero_2 =', resultado)

print()

# Operador a nivel de bits not: ~
print('Operador a nivel de bits not: ~')

numero = 5 # 101

# 101 ~
# ===
# -(101 + 1)
# -(110)
# -(6)
# -6

resultado = ~numero

print('~numero =', resultado)

print()

# Operador a nivel de bits xor: ^
print('Operador a nivel de bits xor: ^')

numero_1 = 5 # 101
numero_2 = 2 # 10

# 101
# 010 ^
# ===
# 111 [2] = 7 [10]

resultado = numero_1 ^ numero_2

print('numero_1 ^ numero_2 =', resultado)

print()

# Operador a nivel de bits - desplazamiento a la derecha: >>
print('Operador a nivel de bits - desplazamiento a la derecha: >>')

numero = 10 # 1010

# 1010 >> 1 = 0101

resultado = numero >> 1
print('numero >> 1 =', resultado)

print()

# Operador a nivel de bits - desplazamiento a la izquierda: <<
print('Operador a nivel de bits - desplazamiento a la izquierda: <<')

numero = 10 # 1010

# 1010 << 1 = 10100

# 2 ^ 4 + 2 ^ 2 = 16 + 4 = 20

resultado = numero << 1
print('numero << 1 =', resultado)
