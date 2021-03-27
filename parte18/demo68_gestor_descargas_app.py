import tkinter as tk
import threading

class GestorDescargasApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Gestor Descargas')
        self.geometry('600x200')
        self.resizable(0, 0)

        frm_superior = tk.Frame(self)
        frm_superior.columnconfigure(0, weight=2)
        frm_superior.columnconfigure(1, weight=10)

        lbl_url = tk.Label(frm_superior, text='URL:', width=10, justify=tk.LEFT, anchor="w")
        lbl_url.grid(row=0, column=0, sticky=tk.W)

        self.url = tk.StringVar(self)
        self.txt_url = tk.Entry(frm_superior, textvariable=self.url, width=80)
        self.txt_url.grid(row=0, column=1, sticky=tk.EW)

        lbl_destino = tk.Label(frm_superior, text='Destino:', width=10, justify=tk.LEFT, anchor="w")
        lbl_destino.grid(row=1, column=0, sticky=tk.W, pady=10)

        self.destino = tk.StringVar(self)
        self.txt_destino = tk.Entry(frm_superior, textvariable=self.url, width=80)
        self.txt_destino.grid(row=1, column=1, sticky=tk.EW, pady=10)

        frm_superior.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=15)

        frm_inferior = tk.Frame(self)
        frm_inferior.columnconfigure(0, weight=1)

        lbl_estado = tk.Label(frm_inferior, text='Listo', width=10, justify=tk.LEFT, anchor="w")
        lbl_estado.grid(row=0, column=0, sticky=tk.W, pady=10)

        btn_seleccionar_destino = tk.Button(frm_inferior, text='Seleccionar destino...')
        btn_seleccionar_destino['command'] = self.seleccionar_destino
        btn_seleccionar_destino.grid(row=0, column=1, sticky='E')
        
        btn_iniciar_descarga = tk.Button(frm_inferior, text='Iniciar descarga')
        btn_iniciar_descarga['command'] = self.iniciar_descarga
        btn_iniciar_descarga.grid(row=0, column=2, sticky='E')

        frm_inferior.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=20)
    
    def seleccionar_destino(self):
        pass
    
    def iniciar_descarga(self):
        pass

def main():
    app = GestorDescargasApp()
    app.mainloop()

if __name__ == '__main__':
    main()
