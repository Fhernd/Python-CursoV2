class Camion(Carro):
    def __init__(self, placa, marca, modelo, pais_procedencia, capacidad_carga):
        super().__init__(self, placa, marca, modelo, pais_procedencia)

        self.capacidad_carga = capacidad_carga
    