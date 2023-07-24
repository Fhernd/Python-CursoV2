import sqlite3


def conectar(nombre_archivo_bd):
    """
    Crea una conexión con la base de datos.

    Parameters:
    nombre_archivo_bd: nombre del archivo de la base de datos.

    Returns:
    Conexión con la base de datos.
    """
    conexion = sqlite3.connect(nombre_archivo_bd)
    conexion.row_factory = sqlite3.Row

    return conexion
