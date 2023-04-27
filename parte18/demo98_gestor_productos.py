import sqlite3
import tkinter as tk
import tkinter.ttk as ttk


class Producto:
    def __init__(self, id, nombre, descripcion, categoria, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio



