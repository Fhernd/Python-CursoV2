from .animal import Animal

class Pato(Animal):
    def __init__(self, nombre, edad, nombre_cientifico, color):
        super().__init__(nombre, edad, nombre_cientifico)

        self.color = color
    
    def volar(self):
        print('El pato está volando...')
    
    def hablar(self):
        print('¡Cuá cuá!')
