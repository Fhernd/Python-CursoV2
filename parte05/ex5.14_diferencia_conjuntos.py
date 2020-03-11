# Ejercicio 5.14: Calcular la diferencia entre dos conjuntos.

escritorio = {'Notepad++', 'Atom', 'Eclipse', 'NetBeans', 'PyCharm'}
portatil = {'Notepad++', 'PyCharm', 'Visual Studio Code', 'IntelliJ IDEA'}

resultado = escritorio.difference(portatil)

print('Los programas que hacen falta en el computador portátil son:', resultado)

print()

resultado = portatil.difference(escritorio)
print('Los programas que hacen falta en el computador de escritorio son:', resultado)
