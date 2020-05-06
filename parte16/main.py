# Creación de objetos (instanciación):

from modelos.carro import Carro
from modelos.camion import Camion

def main():
    carro_chevrolet = Carro('ABC-123', 'Chevrolet', 2010, 'Estados Unidos')

    print('El tipo de dato de la variable `carro_chevrolet` es:', type(carro_chevrolet).__name__)

    print()

    print('Contenido de las variables de instancia de la clase Carro:')
    print('Placa:', carro_chevrolet.placa)
    print('Marca:', carro_chevrolet.marca)
    print('Modelo:', carro_chevrolet.modelo)
    print('País procedencia:', carro_chevrolet.pais_procedencia)
    print('¿Está encendido?:', 'Sí' if carro_chevrolet.estado else 'No')

    print()

    print('Invocación de métodos de instancia de la clase Carro:')

    carro_chevrolet.encender()

    print('¿Está encendido?:', 'Sí' if carro_chevrolet.estado else 'No')

    carro_chevrolet.apagar()

    print('¿Está encendido?:', 'Sí' if carro_chevrolet.estado else 'No')

    print()

    carro_chevrolet.acelerar()
    carro_chevrolet.frenar()

    carro_chevrolet.encender()

    carro_chevrolet.acelerar()
    carro_chevrolet.frenar()

    print()

    # Creación/instanciación de un objeto Camion:

    camion_carga = Camion('ABD-456', 'Scania', 2015, 'China', 2000)

    print('El tipo de dato de la variable `camion_carga` es:', type(camion_carga))

    print('Placa:', camion_carga.placa)
    print('Marca:', camion_carga.marca)
    print('Modelo:', camion_carga.modelo)
    print('País procedencia:', camion_carga.pais_procedencia)
    print('¿Está encendido?:', 'Sí' if camion_carga.estado else 'No')
    print('Capacidad de carga (kg):', camion_carga.capacidad_carga)

if __name__ == '__main__':
    main()
