import tkinter as tk


class AppCursores(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Cursores Mouse')
        self.geometry('300x300')
        self.resizable(0, 0)

        self.lbl_estado = tk.Label(self, text='Click en cualquier botón para iniciar...')

        self.btn_iniciar = tk.Button(self, text='¡Iniciar!')
        self.btn_iniciar['command'] = self.inicializar_gui

        self.btn_ayuda = tk.Button(self, text='Ayuda', cursor='question_arrow')
    
    def iniciar(self):
        pass


def main():
    app = AppCursores()
    app.mainloop()


if __name__ == '__main__':
    main()
