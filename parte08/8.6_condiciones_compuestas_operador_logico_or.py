# Condición compuesta con el operador or (O lógico):

agnios_experiencia = int(input('Escriba la cantidad de años de experiencia programando: '))
lenguaje = input('Escriba el lenguaje de programación que domina: ')

if agnios_experiencia >= 5 or lenguaje in ['Python', 'Java', 'JavaScript']:
    print('Ud. ha calificado para trabajar con nosotros.')
else:
    print('Ud. puede intentar en otra ocasión.')
