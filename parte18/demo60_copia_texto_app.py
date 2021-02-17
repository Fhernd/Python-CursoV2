import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class CopiaTextoApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.txa_origen = st.ScrolledText(self, width=50, height=10)
        self.txa_origen.grid(column=0, row=0, padx=10, pady=10)

        self.lfm_seleccion = ttk.LabelFrame(self, text='Selección')
        self.lfm_seleccion.grid(column=0, row=1, padx=5, pady=5, sticky='w')

        lbl_fila_origen = ttk.Label(self.lfm_seleccion, text='Desde fila:')
        lbl_fila_origen.grid(column=0, row=0, padx=5, pady=5, sticky='e')
        self.fila_origen = tk.StringVar()
        self.txt_fila_origen = ttk.Entry(self.lfm_seleccion, textvariable=self.fila_origen)
        self.txt_fila_origen.grid(row=0, column=1, padx=5, pady=5, sticky='e')
        
        lbl_columna_origen = ttk.Label(self.lfm_seleccion, text='Desde columna:')
        lbl_columna_origen.grid(column=0, row=1, padx=5, pady=5, sticky='e')
        self.columna_origen = tk.StringVar()
        self.txt_columna_origen = ttk.Entry(self.lfm_seleccion, textvariable=self.columna_origen)
        self.txt_columna_origen.grid(column=1, row=1, padx=5, pady=5, sticky='e')

        lbl_fila_destino = ttk.Label(self.lfm_seleccion, text='Hasta fila:')
        lbl_fila_destino.grid(column=0, row=2, padx=5, pady=5, sticky='e')
        self.fila_destino = tk.StringVar()
        self.txt_fila_origen = ttk.Entry(self.lfm_seleccion, textvariable=self.fila_destino)
        self.txt_fila_origen.grid(column=1, row=2, padx=5, pady=5, sticky='e')
        
        lbl_columna_destino = ttk.Label(self.lfm_seleccion, text='Hasta columna:')
        lbl_columna_destino.grid(column=0, row=3, padx=5, pady=5, sticky='e')
        self.columna_destino = tk.StringVar()
        self.txt_columna_origen = ttk.Entry(self.lfm_seleccion, textvariable=self.columna_destino)
        self.txt_columna_origen.grid(column=1, row=3, padx=5, pady=5, sticky='e')

        btn_copiar = ttk.Button(self.lfm_seleccion, text='Copiar', command=self.copiar)
        btn_copiar.grid(column=1, row=4, padx=10, pady=10)

        self.txa_destino = st.ScrolledText(self, width=50, height=10)
        self.txa_destino.grid(column=0, row=2, padx=10, pady=10)
    
    def copiar(self):
        pass

def main():
    app = CopiaTextoApp()
    app.mainloop()

if __name__ == '__main__':
    main()
