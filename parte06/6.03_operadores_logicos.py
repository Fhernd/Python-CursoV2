# Operadores Lógicos

# Operador lógico Y: and

edad = 19
nombre = 'Daniela'

resultado = edad >= 18 and nombre == 'Daniela'
print('¿La persona se llama Daniela y es mayor de edad?: {}'.format(resultado))

edad = 17
resultado = edad >= 18 and nombre == 'Daniela'
print('¿La persona se llama Daniela y es mayor de edad?: {}'.format(resultado))

print()

# Operador Lógico O: or

edad = 23
profesion = 'Programador'

califica = edad > 20 or profesion == 'Programador'
print('¿La persona tiene más de 20 años o es programadora?:', califica)

edad = 17
profesion = 'Ingeniero'

califica = edad > 20 or profesion == 'Programador'
print('¿La persona tiene más de 20 años o es programadora?:', califica)
