class Carro:
    def __init__(self, placa, marca, modelo, pais_procedencia):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.pais_procedencia = pais_procedencia
        self.estado = False
    
    def encender(self):
        if not self.estado:
            self.estado = True
    
    def apagar(self):
        if self.estado:
            self.estado = False
    
    def acelerar(self):
        if self.estado:
            print('El carro ha acelerado')
    
    def frenar(self):
        if self.estado:
            print('El carro ha frenado')
