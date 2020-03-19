# Ejercicio 8.10. Validar si tres valores numéricos pueden pertenecer al esquema de colores RGB.

# RGB Rojo, Verde, Azul

rojo = int(input('Digite la cantidad de color rojo (0 - 255): '))
verde = int(input('Digite la cantidad de color verde (0 - 255): '))
azul = int(input('Digite la cantidad de color azul (0 - 255): '))

if 0 <= rojo <= 255 and 0 <= verde <= 255 and 0 <= azul <= 255:
    print('Los valores %i %i %i corresponden para el esquema RGB.' % (rojo, verde, azul))
else:
    print('Los valores %i %i %i NO corresponden para el esquema RGB.' % (rojo, verde, azul))
