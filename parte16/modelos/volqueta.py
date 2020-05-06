from . carro import Carro

class Volqueta(Carro):
    def __init__(self, placa, marca, modelo, pais_procedencia, capacidad_carga, costo_servicio):
        super().__init__(placa, marca, modelo, pais_procedencia)

        self.capacidad_carga = capacidad_carga
        self.costo_servicio = costo_servicio
    
    def cargar_material(self):
        print('Se está cargando el material en la volqueta...')
    
    def descargar_material(self):
        print('Se está descargando el material desde la volqueta...')
