import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class EditorTextoAplicacion(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.area_texto = tk.Text(self.master)
        
        frm_botones = tk.Frame(self.master, relief=tk.RAISED, bd=2)
        btn_abrir = tk.Button(frm_botones, text='Abrir...', command=self.abrir_archivo)
        btn_guardar = tk.Button(frm_botones, text='Guardar...', command=self.guardar_archivo)

        btn_abrir.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        btn_guardar.grid(row=1, column=0, sticky='ew', padx=5)

        frm_botones.grid(row=0, column=0, sticky='ns')
        self.area_texto.grid(row=0, column=1, sticky='nsew')
    
    def abrir_archivo(self):
        ruta_archivo = askopenfilename(filetypes=[('Archivo de texto', ('*.txt'))])

        if not ruta_archivo:
            return
        
        self.area_texto.delete(1.0, tk.END)

        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            self.area_texto.insert(tk.END, contenido)
        
        self.master.title(f'Editor de texto - {ruta_archivo}')

    def guardar_archivo(self):
        ruta_archivo = asksaveasfilename(defaultextension='txt', filetypes=[('Archivos de texto', '*.txt')])

        if not ruta_archivo:
            return
        
        with open(ruta_archivo, 'wt', encoding='utf-8') as f:
            contenido = self.area_texto.get(1.0, tk.END)
            f.write(contenido)
        
        self.master.title(f'Editor de texto - {ruta_archivo}')

def main():
    root = tk.Tk()
    root.title('Editor de texto')
    root.geometry('480x400')

    ventana = EditorTextoAplicacion(root)
    ventana.mainloop()

if __name__ == "__main__":
    main()
