from datetime import timedelta, datetime
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class Contacto:
    
    def __init__(self, nombre, email, fecha_nacimiento):
        self.nombre = nombre
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
    
    def __str__(self):
        return f'{self.email};{self.nombre};{self.fecha_nacimiento}'

class GestionContactos:
    
    def __init__(self):
        self.nombre_archivo = 'parte18/demo42_contactos.txt'

        self.verificar_archivo()
    
    def verificar_archivo(self):
        if not os.path.exists(self.nombre_archivo):
            with open(self.nombre_archivo, 'wt', encoding='utf-8') as f:
                pass