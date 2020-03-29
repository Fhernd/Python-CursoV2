# Ejercicio 11.5: A través de una función validar si un número se halla en un rango.

def valor_en_rango(valor, rango):
    """
    Comprueba si un valor dado se halla en un rango específico.

    Parameters:
    valor: Valor a verificar.
    rango: Rango de valores.

    Returns:
    True: si el valor se halla en el rango, False en caso contrario.
    """
    if isinstance(valor, (int, float)):
        if isinstance(rango, (list, tuple)):
            if len(rango) == 2:
                inicio = rango[0]
                fin = rango[1]

                if inicio < fin:
                    return valor in range(inicio, fin + 1)

                raise ValueError('El rango debe estar compuestos por dos números: el primero debe ser menor al segundo.')

            raise Exception('El rango debe tener exactamente dos (2) elementos.')

        raise TypeError('Ha especificado un tipo de valor inválido para el argumento `rango`. Debe ser una lista o tupla.')
    
    raise TypeError('Ha especificado un tipo de valor inválido para el argumento `valor`. Debe ser un entero o real.')


numero = 5
rango = [0, 10]

try:
    resultado = valor_en_rango(numero, rango)
    print('¿El valor {} se halla en el rango {}? {}'.format(numero, rango, resultado))
except Exception as e:
    print('ERROR:', e)

print()

numero = 5
rango = [10, 0]

try:
    resultado = valor_en_rango(numero, rango)
    print('¿El valor {} se halla en el rango {}? {}'.format(numero, rango, resultado))
except Exception as e:
    print('ERROR:', e)
