import tkinter as tk


class FormularioRegistro(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Formulario Registro')
        self.geometry('300x300')

        lfm_informacion_personal = tk.LabelFrame(self, padx=15, pady=10, text='Información personal')
        lfm_informacion_personal.pack(padx=10, pady=5)

        tk.Label(lfm_informacion_personal, text='Primer nombre').grid(row=0)
        tk.Label(lfm_informacion_personal, text='Primer apellido').grid(row=1)

        tk.Entry(lfm_informacion_personal).grid(row=0, column=1, sticky=tk.W)
        tk.Entry(lfm_informacion_personal).grid(row=1, column=1, sticky=tk.W)

        lfm_ubicacion = tk.LabelFrame(self, padx=15, pady=10, text='Ubicación')
        lfm_ubicacion.pack(padx=10, pady=5)

        tk.Label(lfm_ubicacion, text='Dirección').grid(row=0)
        tk.Label(lfm_ubicacion, text='Ciudad').grid(row=1)
        tk.Label(lfm_ubicacion, text='Código postal').grid(row=2)

        tk.Entry(lfm_ubicacion).grid(row=0, column=1, sticky=tk.W)
        tk.Entry(lfm_ubicacion).grid(row=1, column=1, sticky=tk.W)
        tk.Entry(lfm_ubicacion, width=8).grid(row=2, column=1, sticky=tk.W)

        btn_registrar = tk.Button(self, text='Registrar')
        btn_registrar.pack(padx=10, pady=10, side=tk.RIGHT)


def main():
    app = FormularioRegistro()
    app.mainloop()


if __name__ == '__main__':
    main()
