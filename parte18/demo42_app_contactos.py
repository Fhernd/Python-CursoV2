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
        try:
            with open(self.nombre_archivo, 'wt', encoding='utf-8') as f:
                for c in contactos:
                    f.write(c)
                    f.write('\n')
            return True
        except:
            return False
    
    def modificar_contacto(self, email, contacto):
        contactos = self.obtener_contactos()

        indice = 0

        for c in contactos:
            if c.email == email:
                c.nombre = contacto.nombre
                c.fecha_nacimiento = contacto.fecha_nacimiento
                self.reemplazar_archivo(contactos)
                
                return True
        
        return False

class ContactosApp:

    def __init__(self, master):
        self.master = master
        self.gestion_contactos = GestionContactos()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        lbl_titulo = tk.Label(self.master, text='Contactos App', font=('Helvetica', 18))
        lbl_titulo.place(x=10, y=10)

        self.lbx_contactos = tk.Listbox(self.master, width=30, height=20)
        self.lbx_contactos.place(x=10, y=40)
        self.lbx_contactos.bind('<<ListboxSelect>>', self.seleccionar_contacto)

        lbl_nombre = tk.Label(self.master, text='Nombre:', font=('Helvetica', 13))
        lbl_nombre.place(x=230, y=40)
        self.txt_nombre = tk.Entry(self.master, width=200)
        self.txt_nombre.place(x=230, y=60)
    
    def seleccionar_contacto(self):
        pass
