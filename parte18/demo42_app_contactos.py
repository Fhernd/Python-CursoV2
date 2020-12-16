from datetime import timedelta, datetime
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class Contacto:
    
    def __init__(self, email, nombre, fecha_nacimiento):
        self.email = email
        self.nombre = nombre
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
    
    def agregar_contacto(self, contacto):
        try:
            with open(self.nombre_archivo, 'at', encoding='utf-8') as f:
                f.write(contacto)
                f.write('\n')

            return True
        except:
            return False
    
    def existe_contacto(self, email):
        for c in self.obtener_contactos:
            if c.email == email:
                return True
        
        return False
    
    def obtener_contactos(self):
        try:
            contactos = []
            with open(self.nombre_archivo, 'rt', encoding='utf-8') as f:
                for l in f.readlines():
                    partes = l.split(';')
                    contacto = Contacto(*partes)
                    contactos.append(contacto)

            return contactos
        except:
            return None
    
    def buscar_contacto_por_email(self, email):
        for c in self.obtener_contactos:
            if c.email == email:
                return c
        
        return None
    
    def eliminar_contacto_por_email(self, email):
        contactos = self.obtener_contactos

        for c in contactos:
            if c.email == email:
                contactos.remove(c)
                reemplazar_archivo(contactos)
                return True
        
        return False
    
    def reemplazar_archivo(self, contactos):
        pass