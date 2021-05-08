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


def main():
    app = FormularioRegistro()
    app.mainloop()


if __name__ == '__main__':
    main()
