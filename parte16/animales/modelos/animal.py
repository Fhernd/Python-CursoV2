class Animal:
    def __init__(self, nombre, edad, nombre_cientifico):
        self.nombre = nombre
        self.edad = edad
        self.nombre_cientifico = nombre_cientifico
    
    def comer(self):
        print('El animal está comiendo...')
    
    def moverse(self):
        print('El animal se está moviendo...')
