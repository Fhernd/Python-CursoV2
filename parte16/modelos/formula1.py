from . carro import Carro

class Formula1(Carro):
    def __init__(self, placa, marca, modelo, pais_procedencia, peso):
        super().__init__(placa, marca, modelo, pais_procedencia)

        self.peso = peso
    
    def competir(self):
        print('El auto ingresa a la pista de carrera...')