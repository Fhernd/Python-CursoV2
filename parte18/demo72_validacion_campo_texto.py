import re
import tkinter as tk


class AplicacionValidacion(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Validación Campo Texto')
        self.geometry('200x200')

        patron = r'^\w{0,10}$'
        self.regex_validacion = re.compile(patron)

        lbl_usuario = tk.Label(self, text='Ingrese su usuario:')
        validador = (self.register(self.validar), '%i', '%P')

        self.txt_usuario = tk.Entry(self, validate='key', validatecommand=validador, invalidcommand=self.invalidar)

        self.lbl_resultado_validacion = tk.Label(self, text='')

        lbl_usuario.pack()
        self.lbl_resultado_validacion.pack()
        self.txt_usuario.pack(anchor=tk.W, padx=10, pady=10)
    
    def validar(self, indice, usuario):
        resultado = self.regex_validacion.match(usuario) is not None

        if resultado:
            self.lbl_resultado_validacion.config(text='')

        return resultado

    def invalidar(self):
        self.lbl_resultado_validacion.config(text='Dato inválido')


def main():
    app = AplicacionValidacion()
    app.mainloop()


if __name__ == '__main__':
    main()
