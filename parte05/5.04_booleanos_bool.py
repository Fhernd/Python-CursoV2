# Falso => False
# Verdadero => True

llueve = False
print(type(llueve))
print(llueve)
if llueve:
    print('El día está lluvioso.')
else:
    print('El día está espléndido.')

print()

llueve = not llueve
print(type(llueve))
print(llueve)

if llueve:
    print('El día está lluvioso.')
else:
    print('El día está espléndido.')

print()

# Operaciones con variables o valores booleanos (lógicos):
llave_1 = True
llave_2 = False

# Operadores lógicos: and (conjunción - y), or (disyunción - o)
print(llave_1 and llave_2)
print(llave_1 and not llave_2)
print(llave_2 or llave_1)
print(llave_2 or not llave_1)

print()

if llave_1 and llave_2:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

if llave_1 and not llave_2:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

if llave_1 or llave_2:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

if not llave_1 or llave_2:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

print('Uso de la clase bool():')
x = bool(1)
print(type(x))
print(x)

print()

x = bool(123)
print(type(x))
print(x)

print()

x = bool(-123)
print(type(x))
print(x)

print()

x = bool(0)
print(type(x))
print(x)

print()

x = bool('False')
print(type(x))
print(x)

x = bool('True')
print(type(x))
print(x)

print()

x = bool(123 < 124)
print(type(x))
print(x)

x = 123 > 124
print(type(x))
print(x)
