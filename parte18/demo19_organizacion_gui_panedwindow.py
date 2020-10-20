import tkinter as tk

class OrganizacionInterfaz(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        organizador = tk.PanedWindow(self, orient='vertical')

        btn_mostrar_mensaje = tk.Button(organizador, text='Mostrar mensaje')
        btn_mostrar_mensaje.pack(side=tk.TOP)
        organizador.add(btn_mostrar_mensaje)

        organizador.pack(fill=tk.BOTH, expand=True)

def main():
    app = tk.Tk()
    app.title('Interfaz Organizada')
    app.geometry('300x300')

    ventana = OrganizacionInterfaz(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
