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
