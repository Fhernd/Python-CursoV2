# Creación de objetos (instanciación):

from modelos.carro import Carro
from modelos.camion import Camion
from modelos.deportivo import Deportivo
from modelos.volqueta import Volqueta
from modelos.formula1 import Formula1

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
    print('Creación/instanciación de un objeto Camion:')

    camion_carga = Camion('ABD-456', 'Scania', 2015, 'China', 2000)

    print('El tipo de dato de la variable `camion_carga` es:', type(camion_carga))

    print('Placa:', camion_carga.placa)
    print('Marca:', camion_carga.marca)
    print('Modelo:', camion_carga.modelo)
    print('País procedencia:', camion_carga.pais_procedencia)
    print('¿Está encendido?:', 'Sí' if camion_carga.estado else 'No')
    print('Capacidad de carga (kg):', camion_carga.capacidad_carga)

    print()

    camion_carga.encender()

    print('¿Está encendido?:', 'Sí' if camion_carga.estado else 'No')

    camion_carga.apagar()

    print('¿Está encendido?:', 'Sí' if camion_carga.estado else 'No')
    
    camion_carga.cargar_mercancia()
    camion_carga.descargar_mercancia()

    print()

    # Creación/instanciación de un objeto Deportivo:
    print('Creación/instanciación de un objeto Deportivo:')

    deportivo_lujo = Deportivo('DEF-789', 'Audi', 2013, 'Alemania', 'Marca Rines', 'Deportivo')

    print('El tipo de dato de la variable `deportivo_lujo` es:', type(deportivo_lujo))

    print('Placa:', deportivo_lujo.placa)
    print('Marca:', deportivo_lujo.marca)
    print('Modelo:', deportivo_lujo.modelo)
    print('País procedencia:', deportivo_lujo.pais_procedencia)
    print('¿Está encendido?:', 'Sí' if deportivo_lujo.estado else 'No')
    print('Marca rines:', deportivo_lujo.marca_rines)
    print('Tipo:', deportivo_lujo.tipo)

    print()

    deportivo_lujo.encender()

    print('¿Está encendido?:', 'Sí' if deportivo_lujo.estado else 'No')

    deportivo_lujo.abrir_puertas()
    deportivo_lujo.cerrar_puertas()

    print()

    deportivo_lujo.acelerar()
    deportivo_lujo.acelerar()

    deportivo_lujo.frenar()

    print()

    # Creación/instanciación de un objeto Volqueta:
    print('Creación/instanciación de un objeto Volqueta:')

    volqueta_carga = Volqueta('FGH-951', 'Daewoo', 2014, 'Taiwan', 4000, 2000000)

    print('El tipo de dato de la variable `volqueta_carga`:', type(volqueta_carga))

    print('Placa:', volqueta_carga.placa)
    print('Marca:', volqueta_carga.marca)
    print('Modelo:', volqueta_carga.modelo)
    print('País procedencia:', volqueta_carga.pais_procedencia)
    print('¿Está encendida?:', 'Sí' if volqueta_carga.estado else 'No')
    print('Capacidad carga (kg):', volqueta_carga.capacidad_carga)
    print('Costo servicio:', volqueta_carga.costo_servicio)

    print()

    volqueta_carga.encender()

    print('¿Está encendida?:', 'Sí' if volqueta_carga.estado else 'No')

    volqueta_carga.cargar_material()

    volqueta_carga.acelerar()

    volqueta_carga.frenar()

    volqueta_carga.descargar_material()

    volqueta_carga.apagar()

    print('¿Está encendida?:', 'Sí' if volqueta_carga.estado else 'No')

    print()

    # Creación/instanciación de un objeto Formula1:
    print('Creación/instanciación de un objeto Formula1:')

    auto_formula1 = Formula1('F11-458', 'BMW', 2019, 'Alemania', 120)
    
    print('El tipo de dato de la variable `auto_formula1`:', type(auto_formula1))

    print('Placa:', auto_formula1.placa)
    print('Marca:', auto_formula1.marca)
    print('Modelo:', auto_formula1.modelo)
    print('País procedencia:', auto_formula1.pais_procedencia)
    print('¿Está encendido?:', 'Sí' if auto_formula1.estado else 'No')
    print('Peso (kg):', auto_formula1.peso)

    print()

    auto_formula1.encender()

    print('¿Está encendido?:', 'Sí' if auto_formula1.estado else 'No')

    auto_formula1.acelerar()
    auto_formula1.competir()
    auto_formula1.frenar()

    auto_formula1.apagar()

    print('¿Está encendido?:', 'Sí' if auto_formula1.estado else 'No')

    print()

    # Iterar por cada uno de los objetos carro que se crearon:
    print('Iterar por cada uno de los objetos carro que se crearon:')
    print()
    carros = [camion_carga, deportivo_lujo, volqueta_carga, auto_formula1]

    for c in carros:
        print('Placa:', c.placa)
        print('Marca:', c.marca)
        print('Modelo:', c.modelo)
        print('País procedencia:', c.pais_procedencia)
        print('¿Está encendido?:', 'Sí' if c.estado else 'No')

        c.encender()
        print('¿Está encendido?:', 'Sí' if c.estado else 'No')

        c.acelerar()
        c.frenar()
        c.apagar()

        print()

if __name__ == '__main__':
    main()
