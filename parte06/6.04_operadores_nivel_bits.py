# Operadores a nivel de bits (bitwise):
print('Operadores a nivel de bits:')

# Operador and: &

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

numero = 5 # 101

# 101 ~
# ===
# -(101 + 1)
# -(110)
# -(6)
# -6

resultado = ~numero

print('~numero =', resultado)
