'''
Ejercicio 4.2: Mostrar en pantalla la fecha y hora actuales del sistema.
'''

import datetime

ahora = datetime.datetime.now()

print('Fecha y hora actuales:', ahora)

print(type(ahora))

print()

ahora_formato = ahora.strftime('%H:%M:%S %d-%m-%Y')
print(ahora_formato)
