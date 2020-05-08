from modelos.rectangulo import Rectangulo
from modelos.circulo import Circulo
from modelos.triangulo import Triangulo

def main():
    # Prueba de ejecución sobre la jerarquía de herencia de figuras - polimorfismo:
    print('Prueba de ejecución sobre la jerarquía de herencia de figuras - polimorfismo:')

    figuras = []

    rectangulo_rojo = Rectangulo('Rojo', 'Negro', 10, 5)

    circulo_verde = Circulo('Verde', 'Negro', 5)

    triangulo_negro = Triangulo('Negro', 'Gris', 7, 10)

    figuras.append(rectangulo_rojo)
    figuras.append(circulo_verde)
    figuras.append(triangulo_negro)

    print()

    print('El área de todas las figuras:')
    for f in figuras:
        f.dibujar()

        area = f.area()
        print(f'El área es igual a {area} u^2')

        print()
    
    print()

    # Demostración de sobreescritura de métodos:
    print('Demostración de sobreescritura de métodos:')

    print(rectangulo_rojo)

    print()

    print(circulo_verde)

    print()

    print(triangulo_negro)

if __name__ == '__main__':
    main()
