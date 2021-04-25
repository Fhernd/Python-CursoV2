import tkinter as tk


class EventosTecladoApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Eventos Teclado')
        self.geometry('400x400')

        txt_campo = tk.Entry(self)
        txt_campo.pack(padx=20, pady=20)

        txt_campo.bind('<FocusIn>', self.mostrar_info_evento)
        txt_campo.bind('<Key>', self.mostrar_tecla_presionada)

    def mostrar_info_evento(self, evento):
        print('Info evento FocusIn')
    
    def mostrar_tecla_presionada(self, evento):
        datos = (evento.keysym, evento.keycode, evento.char)

        print(datos)


def main():
    app = EventosTecladoApp()
    app.mainloop()


if __name__ == '__main__':
    main()
