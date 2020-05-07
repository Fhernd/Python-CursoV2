from . carro import Carro

class Deportivo(Carro):
    def __init__(self, placa, marca, modelo, pais_procedencia, marca_rines, tipo):
        super().__init__(placa, marca, modelo, pais_procedencia)

        self.marca_rines = marca_rines
        self.tipo = tipo
    
    def abrir_puertas(self):
        print('Las puertas se están abriendo...')

    def cerrar_puertas(self):
        print('Las puertas se están cerrando...')
