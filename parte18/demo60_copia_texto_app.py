import tkinter as tk
from tkinter import messagebox
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
        fila_origen = self.fila_origen.get().strip()

        if len(fila_origen) == 0:
            messagebox.showwarning('Mensaje', 'El campo Desde fila es obligatorio.')
            return
        
        columna_origen = self.columna_origen.get().strip()

        if len(columna_origen) == 0:
            messagebox.showwarning('Mensaje', 'El campo Desde columna es obligatorio.')
            return
        
        fila_destino = self.fila_destino.get().strip()

        if len(fila_destino) == 0:
            messagebox.showwarning('Mensaje', 'El campo Hasta fila es obligatorio.')
            return
        
        columna_destino = self.columna_destino.get().strip()

        if len(columna_destino) == 0:
            messagebox.showwarning('Mensaje', 'El campo Hasta columna es obligatorio.')
            return
        
        try:
            fila_origen = int(fila_origen)
        except:
            messagebox.showwarning('Mensaje', 'El campo Desde fila debe ser un número entero.')
            return
        
        try:
            columna_origen = int(columna_origen)
        except:
            messagebox.showwarning('Mensaje', 'El campo Desde columna debe ser un número entero.')
            return
        
        try:
            fila_destino = int(fila_destino)
        except:
            messagebox.showwarning('Mensaje', 'El campo Hasta fila debe ser un número entero.')
            return
        
        try:
            columna_destino = int(columna_destino)
        except:
            messagebox.showwarning('Mensaje', 'El campo Hasta columna debe ser un número entero.')
            return

        if fila_origen >= 1 and columna_origen >= 1 and fila_destino >= 1 and columna_destino >= 1:
            texto_seleccionado = self.txa_origen.get('1.0', tk.END)

            lineas = texto_seleccionado.split('\n')
            resultado = []

            fila_origen -= 1
            columna_origen -= 1
            fila_destino -= 1

            for i in range(fila_origen, fila_destino + 1):
                l = lineas[i].strip()

                if len(l):
                    resultado.append(l[columna_origen: columna_destino if columna_destino <= len(l) else len(l)])

            self.txa_destino.delete('1.0', tk.END)

            self.txa_destino.insert('1.0', '\n'.join(resultado))
        else:
            messagebox.showwarning('Mensaje', 'Los campos de Selección deben ser números positivos.')
            return

def main():
    app = CopiaTextoApp()
    app.mainloop()

if __name__ == '__main__':
    main()
