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
