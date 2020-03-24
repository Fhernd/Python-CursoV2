# Creación de una clase de excepción personalizada:

class ValorMinimoError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return 'ValorMinimoError: {}'.format(self.message)
        else:
            return 'Se ha generado el error ValorMinimoError.'

class ValorMaximoError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return 'ValorMaximoError: {}'.format(self.message)
        else:
            return 'Se ha generado el error ValorMaximoError.'


minimo = 10
maximo = 20

while True:
    try:
        numero = int(input('Escriba un número entre {} y {}: '.format(minimo, maximo)))

        if numero < minimo:
            raise ValorMinimoError('Ha escrito un valor menor a {}.'.format(minimo))
        elif numero > maximo:
            raise ValorMaximoError('Ha escrito un valor mayor a {}.'.format(maximo))
        
        print('Ha escrito un entre {} y {}.'.format(minimo, maximo))

        break
    except ValueError:
        print('Debe escribir un valor entero válido.')
    except ValorMinimoError as e:
        print('ERROR:', e)
    except ValorMaximoError as e:
        print('ERROR:', e)
    
    print()
