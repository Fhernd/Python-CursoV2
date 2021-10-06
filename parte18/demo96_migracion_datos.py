import csv
import sqlite3
from sqlite3.dbapi2 import connect


def main():
    with open('parte18/demo95_contactos.csv') as f, \
        sqlite3.connect('parte18/demo96_contactos.db') as conexion:

        conexion.execute("""
            CREATE TABLE contacto (
                apellidos TEXT,
                nombres TEXT,
                email TEXT,
                telefono TEXT
            );
        """)

        conexion.executemany('INSERT INTO contacto VALUES (?, ?, ?, ?)', csv.reader(f))

if __name__ == '__main__':
    main()
