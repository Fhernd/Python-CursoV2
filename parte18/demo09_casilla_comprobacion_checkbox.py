import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.estado_participacion_encuesta = tk.IntVar()
        self.chk_participar_encuesta = tk.Checkbutton(self, text='¿Desea participar en la encuesta?', variable=self.estado_participacion_encuesta)
        self.chk_participar_encuesta.grid(row=0,column=0)

        btn_verificar_respuesta = tk.Button(self, text='Validar respuesta')
        btn_verificar_respuesta['command'] = self.verificar_respuesta
        btn_verificar_respuesta.grid(row=0, column=1)
    
    def verificar_respuesta(self):
        if self.estado_participacion_encuesta.get():
            messagebox.showinfo('Mensaje', 'Gracias por participar en la encuesta.')
        else:
            messagebox.showinfo('Mensaje', 'Esperamos que la próxima vez participe en la encuesta.')

def main():
    app = tk.Tk()
    app.title('Encuesta')
    app.geometry('400x300')

    ventana = VentanaPrincipal(app)

    ventana.mainloop()

if __name__ == "__main__":
    main()
