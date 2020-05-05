# Creación de objetos (instanciación):

from parte16.modelos import Carro

def main():
    carro_chevrolet = Carro('ABC-123', 'Chevrolet', 2010, 'Estados Unidos')

    print('El tipo de dato de la variable `carro` es:', type(carro_chevrolet))

if __name__ == '__main__':
    main()
