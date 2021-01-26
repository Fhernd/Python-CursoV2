from tkinter import messagebox, Button, Tk, BOTTOM, LEFT, RIGHT, TOP

class EfectoBotones(object):

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        btn_verde = Button(self.master, text='Verde', activeforeground='white', activebackground='green', pady=10)
        btn_verde['command'] = self.seleccionar_color

        btn_azul = Button(self.master, text='Azul', activeforeground='white', activebackground='blue', pady=10)
        btn_azul['command'] = self.seleccionar_color
        
        btn_amarillo = Button(self.master, text='Amarillo', activeforeground='black', activebackground='yellow', pady=10)
        btn_amarillo['command'] = self.seleccionar_color
        
        btn_rojo = Button(self.master, text='Rojo', activeforeground='white', activebackground='red', pady=10)
        btn_rojo['command'] = self.seleccionar_color

        btn_verde.pack(side=TOP)
        btn_azul.pack(side=RIGHT)
        btn_amarillo.pack(side=BOTTOM)
        btn_rojo.pack(side=LEFT)
    
    def seleccionar_color(self):
        messagebox.showinfo('Mensaje', 'Se ha presionado un botón.')

def main():
    master = Tk()
    master.title('Efecto Botones')
    master.geometry('200x100')

    ventana = EfectoBotones(master)

    master.mainloop()

if __name__ == '__main__':
    main()
