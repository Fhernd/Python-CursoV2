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


class Aplicacion(tk.Tk):

    def __init__(self):
        super().__init__()

        self.lenguajes = ['Python', 'C#', 'JavaScript', 'Go', 'Java', 'C++', 'Kotlin', 'C', 'PHP']

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Selección Lenguajes de Programación')

        self.frm_lenguajes = Lista(self, self.lenguajes)
        self.frm_lenguajes_destino = Lista(self)

        btn_derecha = tk.Button(self, text='>', command=self.pasar_derecha)
        btn_izquierda = tk.Button(self, text='<', command=self.pasar_izquierda)

        self.frm_lenguajes.pack(side=tk.LEFT, padx=10, pady=10)
        self.frm_lenguajes_destino.pack(side=tk.RIGHT, padx=10, pady=10)
        btn_derecha.pack(expand=True, ipadx=5)
        btn_izquierda.pack(expand=True, ipadx=5)

    
    def pasar_derecha(self):
        self.pasar(self.frm_lenguajes, self.frm_lenguajes_destino)

    def pasar_izquierda(self):
        self.pasar(self.frm_lenguajes_destino, self.frm_lenguajes)
    
    def pasar(self, origen, destino):
        dato = origen.extraer_dato()

        if dato:
            destino.insertar_dato(dato)


def main():
    app = Aplicacion()
    app.mainloop()


if __name__ == '__main__':
    main()
