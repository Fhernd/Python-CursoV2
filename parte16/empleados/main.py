from modelos.empleado_comision import EmpleadoComision
from modelos.empleado_horas import EmpleadoHoras
from modelos.empleado_nomina import EmpleadoNomina

def main():
    empleados = []

    jorge = EmpleadoComision('123', 'Jorge Pérez', 'jorge@mail.co', 'Ventas', 0.30, 10000)

    viviana = EmpleadoHoras('987', 'Viviana García', 'viviana@mail.co', 'Diseño Gráfico', 80, 100)

    patricia = EmpleadoNomina('456', 'Patricia Toledo', 'patricia@mail.co', 'Finanzas', 0.10)

    empleados.append(jorge)
    empleados.append(viviana)
    empleados.append(patricia)

    for e in empleados:
        print(e)
        print(f'Salario: {e.calcular_salario()}')

        print()

if __name__ == '__main__':
    main()
