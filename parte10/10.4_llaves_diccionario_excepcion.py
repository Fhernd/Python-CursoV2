# Excepciones a la hora de trabajar con diccionarios.

versiones = {'Python': '3.8.1', 'Java': '12', 'JavaScript': 'ES6', 'C#': '8'}

lenguaje = input('Escriba un nombre de lenguaje de programación: ')

try:
    version = versiones[lenguaje]

    print('La versión de {} es {}'.format(lenguaje, version))
except KeyError as e:
    print('ERROR:', e)

print('Fin del programa.')

print()

# Uso del método `get()`:
print('Uso del método `get()`:')

version = versiones.get('java', '1.0.0')
print('La versión de {} es {}'.format('java', version))
