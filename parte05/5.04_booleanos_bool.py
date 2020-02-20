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
a = True
b = False

# Operadores lógicos: and (conjunción - y), or (disyunción - o)
print(a and b)
print(a and not b)
print(b or a)
print(b or not a)

print()

if a and b:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

if a and not b:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

if a or b:
    print('Sí hay agua')
else:
    print('No hay agua')

print()

if not a or b:
    print('Sí hay agua')
else:
    print('No hay agua')
