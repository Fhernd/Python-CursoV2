from modelos.pato import Pato
from modelos.gato import Gato
from modelos.perro import Perro

def main():
    animales = []

    cua = Pato('Platy', 2, 'Anas platyrhynchos domesticus', 'Verde')

    charlie = Gato('Charlie', 1, 'Felis catus', True)

    mateo = Perro('Mateo', 2, 'Canis lupus familiaris', 'Golden Retriever')

    animales.append(cua)
    animales.append(charlie)
    animales.append(mateo)

    print('Nombres de los animales:')
    for a in animales:
        print('Nombre del animal:', a.nombre)

    print()

    print('El zootecnista les dice a todos los animales que hablen ahora:')

    for a in animales:
        a.hablar()

if __name__ == '__main__':
    main()
