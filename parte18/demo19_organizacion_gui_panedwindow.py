import tkinter as tk

class OrganizacionInterfaz(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        organizador = tk.PanedWindow(self.master, orient='vertical')

        btn_mostrar_mensaje = tk.Button(organizador, text='Mostrar mensaje')
        btn_mostrar_mensaje.pack(side=tk.TOP)
        organizador.add(btn_mostrar_mensaje)
        organizador.pack(fill=tk.BOTH, expand=True)

        chk_activar_accion = tk.Checkbutton(organizador, text='Activar accion')
        chk_activar_accion.pack(side=tk.TOP)
        organizador.add(chk_activar_accion)

        lbl_saludo = tk.Label(organizador, text='¡Tkinter es tremendo!')
        lbl_saludo.pack(side=tk.TOP)
        organizador.add(lbl_saludo)

        txt_nombre = tk.Entry(organizador, text='¡Python es genial!')
        txt_nombre.pack(side=tk.TOP)
        organizador.add(txt_nombre)

        organizador.configure(sashrelief=tk.RAISED)

def main():
    app = tk.Tk()
    app.title('Interfaz Organizada')
    app.geometry('300x150')

    ventana = OrganizacionInterfaz(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
