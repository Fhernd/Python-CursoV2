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
        lbl_titulo = tk.Label(self.master, text='Contactos App', font=('Helvetica', 16))
        lbl_titulo.place(x=10, y=10)

        self.lbx_contactos = tk.Listbox(self.master, width=30, height=20)
        self.lbx_contactos.place(x=10, y=40)
        self.lbx_contactos.bind('<<ListboxSelect>>', self.seleccionar_contacto)

        lbl_nombre = tk.Label(self.master, text='Nombre:', font=('Helvetica', 13))
        lbl_nombre.place(x=230, y=40)
        self.txt_nombre = tk.Entry(self.master, width=48)
        self.txt_nombre.place(x=230, y=70)
        
        lbl_email = tk.Label(self.master, text='Email:', font=('Helvetica', 13))
        lbl_email.place(x=230, y=90)
        self.txt_email = tk.Entry(self.master, width=48)
        self.txt_email.place(x=230, y=120)
        
        lbl_fecha_nacimiento = tk.Label(self.master, text='Fecha nacimiento:', font=('Helvetica', 13))
        lbl_fecha_nacimiento.place(x=230, y=140)
        self.txt_email = tk.Entry(self.master, width=48)
        self.txt_email.place(x=230, y=170)

        lbl_edad = tk.Label(self.master, text='Edad:', font=('Helvetica', 13))
        lbl_edad.place(x=230, y=190)
        self.lbl_edad_agnios = tk.Label(self.master, text='0 años', font=('Helvetica', 13))
        self.lbl_edad_agnios.place(x=230, y=215)

        btn_nuevo = tk.Button(self.master, text='Nuevo', width=18)
        btn_nuevo.place(x=230, y=255)
        btn_nuevo['command'] = self.nuevo
        
        btn_guardar = tk.Button(self.master, text='Guardar', width=18)
        btn_guardar.place(x=385, y=255)
        btn_guardar['command'] = self.guardar
        
        btn_actualizar = tk.Button(self.master, text='Actualizar', width=18)
        btn_actualizar.place(x=230, y=287)
        btn_actualizar['command'] = self.actualizar
        
        btn_eliminar = tk.Button(self.master, text='Guardar', width=18)
        btn_eliminar.place(x=385, y=287)
        btn_eliminar['command'] = self.eliminar

        self.lbl_foto = tk.Label(self.master)
        self.lbl_foto.place(x=550, y=70, width=200, height=200)

    def nuevo(self):
        pass
    
    def guardar(self):
        pass
    
    def actualizar(self):
        pass
    
    def eliminar(self):
        pass
    
    def seleccionar_contacto(self):
        pass

def main():
    app = tk.Tk()
    app.title('Contactos App')
    app.geometry('700x420')

    ventana = ContactosApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()
