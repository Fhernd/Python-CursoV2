from .empleado import Empleado

class EmpleadoNomina(Empleado):
    SALARIO = 2000

    def __init__(self, documento, nombre_completo, correo_electronico, especialidad, porcentaje_prestaciones):
        super().__init__(documento, nombre_completo, correo_electronico, especialidad)

        self.porcentaje_prestaciones = porcentaje_prestaciones
    
    def calcular_salario(self):
        total = super().calcular_salario() + EmpleadoNomina.SALARIO * (1 - self.porcentaje_prestaciones)

        return total
