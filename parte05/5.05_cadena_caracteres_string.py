# Tipo de dato compuesto string

nombre = 'Edward Ortiz'
email = "edward@mail.co"
direccion = '''Carrera 1 # 13A-29
Bogotá - Colombia
GMT-05
'''

print(type(nombre))
print(nombre)

print()

mensaje = 'Bienvenido(a), ' + nombre + '. Correo: ' + email
print(type(mensaje))
print(mensaje)

print()
# Interpolación:
mensaje = f'Bienvenido(a), {nombre}. Correo: {email}'
print(mensaje)

# format() de la clase str:
mensaje = 'Bienvenido(a), {}. Correo: {}'.format(nombre, email)
print(mensaje)

# Formato con %:
mensaje = 'Bienvenido(a), %s. Correo: %s' % (nombre, email)
print(mensaje)

print()

# Inmutabilidad de cadenas de caracteres (str):
lenguaje = "Python"
print(lenguaje)
print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[2])
print(lenguaje[3])
print(lenguaje[4])
print(lenguaje[5])

print()

# lenguaje[0] = 'p' # TypeError

lenguaje = 'p' + lenguaje[1:]
print(lenguaje)

# Inmutables... se dicen que son estáticos

print(id('python') == id('python'))

lenguaje = 'Python'.lower()
print(lenguaje)
