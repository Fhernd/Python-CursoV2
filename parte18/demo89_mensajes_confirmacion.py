import tkinter as tk
import tkinter.messagebox as mb


class Aplicacion(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.title('Diálogos de Confirmación')
        self.geometry('350x250')

        self.crear_boton(mb.askyesno, 'Confirmación Sí/No', 'Respuesta Sí/No')
        self.crear_boton(mb.askquestion, 'Confirmación Pregunta', 'Respuesta Pregunta')
        self.crear_boton(mb.askokcancel, 'Confirmación OK/Cancelar', 'Respuesta OK/Cancelar')
        self.crear_boton(mb.askretrycancel, 'Confirmación Reintentar/Cancelar', 'Respuesta Reintentar/Cancelar')
        self.crear_boton(mb.askyesnocancel, 'Confirmación Sí/No/Cancelar', 'Respuesta Sí/No/Cancelar')

    def crear_boton(self, tipo_dialogo, titulo, mensaje):
        comando = lambda: print(tipo_dialogo(titulo, mensaje))
        btn_comando = tk.Button(self, text=titulo, command=comando)
        btn_comando.pack(padx=40, pady=5, expand=True, fill=tk.BOTH)


def main():
    app = Aplicacion()
    app.mainloop()


if __name__ == '__main__':
    main()
