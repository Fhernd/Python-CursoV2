import tkinter as tk


class Lista(tk.Frame):

    def __init__(self, root, datos=[]):
        super().__init__(root)
        self.datos = datos
        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.lbx_datos = tk.Listbox(self)
        
        self.scl_datos = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.extraer_dato)
        
        self.lbx_datos.config(yscrollcommand=self.scl_datos.set)
        self.lbx_datos.insert(0, *self.datos)
        self.lbx_datos.pack(side=tk.LEFT, fill=tk.Y)
    
    def extraer_dato(self):
        indice = self.lbx_datos.curselection()

        if indice:
            valor = self.lbx_datos.get(indice)
            self.lbx_datos.delete(indice)

            return valor
    
    def insertar_dato(self, dato):
        self.lbx_datos.insert(tk.END, dato)
