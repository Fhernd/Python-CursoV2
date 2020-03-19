# Ejercicio 8.7. Categorizar según la cantidad de puntos obtenidos por un jugador.

# +----------+---------------+
# | Puntos   | Categoría     |
# +----------+---------------+
# | 0-100    | Principiante  |
# +----------+---------------+
# | 101-500  | Estándar      |
# +----------+---------------+
# | 501-2000 | Experimentado |
# +----------+---------------+
# | 2000>    | Máster        |
# +----------+---------------+

puntos = int(input('Digite la cantidad de puntos obtenidos: '))

categoria = None

if puntos <= 100:
    categoria = 'Principiante'
elif puntos <= 500:
    categoria = 'Estándar'
elif puntos <= 2000:
    categoria = 'Experimentado'
else:
    categoria = 'Máster'

print('La categoría del jugador es %s' % categoria)
