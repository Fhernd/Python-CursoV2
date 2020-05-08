from abc import ABC

class Empleado(ABC):
    SALARIO_BASE = 1000

    def __init__(self, documento, nombre_completo, correo_electronico, especialidad):
        self.documento = documento
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.especialidad = especialidad
    
    def calcular_salario(self):
        total = Empleado.SALARIO_BASE * 1.10

        return total

    def __str__(self):
        return f'Documento: {self.documento} - Nombre completo: {self.nombre_completo} - Correo-e: {self.correo_electronico} - Especialidad: {self.especialidad}.'