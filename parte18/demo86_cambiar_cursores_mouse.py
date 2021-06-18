import tkinter as tk


class AppCursores(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Cursores Mouse')
        self.geometry('400x300')
        self.resizable(0, 0)

        self.lbl_estado = tk.Label(self, text='Click en el botón Iniciar...')

        self.btn_iniciar = tk.Button(self, text='¡Iniciar!')
        self.btn_iniciar['command'] = self.perform_action

        self.btn_ayuda = tk.Button(self, text='Ayuda', cursor='question_arrow')

        opciones_botones = {
            'side': tk.LEFT,
            'expand': True,
            'fill': tk.X,
            'ipadx': 30,
            'padx': 20,
            'pady': 5
        }

        self.lbl_estado.pack(pady=10)
        self.btn_iniciar.pack(**opciones_botones)
        self.btn_ayuda.pack(**opciones_botones)
    
    def perform_action(self):
        self.config(cursor='watch')
        self.btn_iniciar.config(state=tk.DISABLED)
        self.btn_ayuda.config(state=tk.DISABLED)
        self.lbl_estado.config(text='Procesando...')
        self.after(5000, self.end_action)
    
    def end_action(self):
        self.config(cursor='arrow')
        self.btn_iniciar.config(state=tk.NORMAL)
        self.btn_ayuda.config(state=tk.NORMAL)
        self.lbl_estado.config(text='Proceso finalizado')


def main():
    app = AppCursores()
    app.mainloop()


if __name__ == '__main__':
    main()
