from . animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad, nombre_cientifico, domestico):
        super().__init__(nombre, edad, nombre_cientifico)

        self.domestico = domestico
    
    def ronronear(self):
        print('El gato está ronroneando...')
    
    def hablar(self):
        print('¡Miau!')
