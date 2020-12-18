from datetime import timedelta, datetime
import datetime
import os
import re
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
    
    def to_str(self):
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
                f.write(contacto.to_str())
                f.write('\n')

            return True
        except Exception as e:
            print(e)
            return False
    
    def existe_contacto(self, email):
        for c in self.obtener_contactos():
            if c.email == email:
                return True
        
        return False
    
    def obtener_contactos(self):
        try:
            contactos = []
            with open(self.nombre_archivo, 'rt', encoding='utf-8') as f:
                for l in f.readlines():
                    partes = l.split(';')
                    contacto = Contacto(partes[0], partes[1], partes[2].strip())
                    contactos.append(contacto)

            return contactos
        except:
            return None
    
    def buscar_contacto_por_email(self, email):
        for c in self.obtener_contactos():
            if c.email == email:
                return c
        
        return None
    
    def eliminar_contacto_por_email(self, email):
        contactos = self.obtener_contactos()

        for c in contactos:
            if c.email == email:
                contactos.remove(c)
                self.reemplazar_archivo(contactos)
                return True
        
        return False
    
    def reemplazar_archivo(self, contactos):
        try:
            with open(self.nombre_archivo, 'wt', encoding='utf-8') as f:
                for c in contactos:
                    f.write(c.to_str())
                    f.write('\n')
            return True
        except:
            return False
    
    def actualizar_contacto(self, email, contacto):
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

        patron = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        self.patron_email = re.compile(patron)

        self.inicializar_gui()

        self.refrescar_lista_contactos()
    
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
        self.txt_fecha_nacimiento = tk.Entry(self.master, width=48)
        self.txt_fecha_nacimiento.place(x=230, y=170)

        lbl_edad = tk.Label(self.master, text='Edad:', font=('Helvetica', 13))
        lbl_edad.place(x=230, y=190)
        self.edad_agnios = tk.StringVar()
        self.lbl_edad_agnios = tk.Label(self.master, text='0 años', font=('Helvetica', 13), textvariable=self.edad_agnios)
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
        
        btn_eliminar = tk.Button(self.master, text='Eliminar', width=18)
        btn_eliminar.place(x=385, y=287)
        btn_eliminar['command'] = self.eliminar

        self.lbl_foto = tk.Label(self.master)
        self.lbl_foto.place(x=550, y=70, width=200, height=200)

    def nuevo(self):
        self.txt_email.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_fecha_nacimiento.delete(0, tk.END)
        self.edad_agnios.set('0 años')
    
    def guardar(self):
        email = self.txt_email.get().strip()
        nombre = self.txt_nombre.get().strip()
        fecha_nacimiento = self.txt_fecha_nacimiento.get().strip()

        if not self.patron_email.search(email):
            messagebox.showwarning('Mensaje', 'Debe escribir un email válido.')
            return
        
        if len(nombre) == 0:
            messagebox.showwarning('Mensaje', 'El campo Nombre es obligatorio.')
            return
        
        try:
            datetime.datetime.strptime(fecha_nacimiento, '%Y/%m/%d')
        except ValueError as e:
            messagebox.showwarning('Mensaje', 'El campo Fecha nacimiento debe tener el formato AAAA/MM/DD.')
            return
        
        if self.gestion_contactos.existe_contacto(email):
            messagebox.showwarning('Mensaje', 'Ya existe un contacto con el email especificado.')
            return
        
        contacto = Contacto(email, nombre, fecha_nacimiento)

        if self.gestion_contactos.agregar_contacto(contacto):
            messagebox.showinfo('Mensaje', 'El contacto se creó de forma satisfactoria.')
            self.nuevo()
            self.refrescar_lista_contactos()
        else:
            messagebox.showwarning('Mensaje', 'Hay problemas con la creación del contacto.')
    
    def actualizar(self):
        email = self.txt_email.get().strip()
        nombre = self.txt_nombre.get().strip()
        fecha_nacimiento = self.txt_fecha_nacimiento.get().strip()

        if not self.patron_email.search(email):
            messagebox.showwarning('Mensaje', 'Debe escribir un email válido.')
            return
        
        if len(nombre) == 0:
            messagebox.showwarning('Mensaje', 'El campo Nombre es obligatorio.')
            return
        
        try:
            datetime.datetime.strptime(fecha_nacimiento, '%Y/%m/%d')
        except ValueError as e:
            messagebox.showwarning('Mensaje', 'El campo Fecha nacimiento debe tener el formato AAAA/MM/DD.')
            return
        
        if not self.gestion_contactos.existe_contacto(email):
            messagebox.showwarning('Mensaje', 'No existe un contacto con el email especificado.')
            return
        
        contacto = Contacto(email, nombre, fecha_nacimiento)

        if self.gestion_contactos.actualizar_contacto(contacto.email, contacto):
            messagebox.showinfo('Mensaje', 'El contacto se actualizó de forma satisfactoria.')
            self.nuevo()
            self.refrescar_lista_contactos()
        else:
            messagebox.showwarning('Mensaje', 'Hay problemas con la actualización del contacto.')
    
    def eliminar(self):
        email = self.txt_email.get().strip()

        if not self.patron_email.search(email):
            messagebox.showwarning('Mensaje', 'Debe escribir un email válido.')
            return
        
        if not self.gestion_contactos.existe_contacto(email):
            messagebox.showwarning('Mensaje', 'No existe un contacto con el email especificado.')
            return
        
        respuesta = messagebox.askquestion('Confirmación', '¿Está seguro de querer eliminar el contacto seleccionado?', icon='warning')

        if respuesta == 'yes':
            if self.gestion_contactos.eliminar_contacto_por_email(email):
                messagebox.showinfo('Mensaje', 'El contacto se eliminó de forma satisfactoria.')
                self.nuevo()
                self.refrescar_lista_contactos()
            else:
                messagebox.showwarning('Mensaje', 'Hay problemas con la eliminación del contacto.')
    
    def seleccionar_contacto(self, evento):
        if self.lbx_contactos.curselection():
            self.contacto_seleccionado = int(self.lbx_contactos.curselection()[0])
            email = self.contactos_emails[self.contacto_seleccionado]
            contacto = self.gestion_contactos.buscar_contacto_por_email(email)

            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, contacto.nombre)
            
            self.txt_email.delete(0, tk.END)
            self.txt_email.insert(0, contacto.email)
            
            self.txt_fecha_nacimiento.delete(0, tk.END)
            self.txt_fecha_nacimiento.insert(0, contacto.fecha_nacimiento.strip())

            self.edad_agnios.set(f'{self.calcular_edad_agnios(contacto.fecha_nacimiento.strip())} años')
    
    def calcular_edad_agnios(self, fecha_nacimiento):
        hoy = datetime.datetime.now()
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y/%m/%d')
        
        edad = hoy.year - fecha_nacimiento.year
        
        if hoy.month < fecha_nacimiento.month:
            edad -= 1
        elif hoy.month == fecha_nacimiento.month and hoy.day < fecha_nacimiento.day: 
            edad -= 1
        
        return edad

    def refrescar_lista_contactos(self):
        contactos = self.gestion_contactos.obtener_contactos()

        self.lbx_contactos.delete(0, tk.END)
        self.contactos_emails = []

        for c in contactos:
            self.lbx_contactos.insert(tk.END, f'{c.nombre} ({c.email})')
            self.contactos_emails.append(c.email)

        self.contacto_seleccionado = -1

def main():
    app = tk.Tk()
    app.title('Contactos App')
    app.geometry('700x420')

    ventana = ContactosApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()
