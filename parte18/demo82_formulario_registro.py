import tkinter as tk


class FormularioRegistro(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Formulario Registro')
        self.geometry('300x300')

        campos = ['Primer nombre', 'Primer apellido', 'Teléfono', 'Email']
        lbl_campos = [tk.Label(self, text=c) for c in campos]
        txt_campos = [tk.Entry(self) for _ in campos]

        self.componentes = list(zip(lbl_campos, txt_campos))

        btn_guardar = tk.Button(self, text='Guardar', command=self.guardar)

        for i, (lbl, txt) in enumerate(self.componentes):
            lbl.grid(row=i, column=0, padx=10, sticky=tk.W)
            txt.grid(row=i, column=1, padx=10, pady=5)
        
        btn_guardar.grid(row=len(self.componentes), column=1, sticky=tk.E, padx=10, pady=10)
    
    def guardar(self):
        for lbl, txt in self.componentes:
            print(f'{lbl.cget("text")} = {txt.get()}')


def main():
    app = FormularioRegistro()
    app.mainloop()


if __name__ == '__main__':
    main()
