from .empleado import Empleado

class EmpleadoComision(Empleado):
    def __init__(self, documento, nombre_completo, correo_electronico, especialidad, porcentaje_comision, monto):
        super().__init__(documento, nombre_completo, correo_electronico, especialidad)

        self.porcentaje_comision = porcentaje_comision
        self.monto = monto
    
    def calcular_salario(self):
        total = super().calcular_salario() + self.monto * self.porcentaje_comision

        return total
