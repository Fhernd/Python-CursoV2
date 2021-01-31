from tkinter import messagebox, IntVar, Label, Menu, Menubutton, Tk

class LenguajesProgramacion(object):

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        lbl_titulo = Label(self.master, text='Lenguajes programación', font='31')
        lbl_titulo.pack()

        mbn_lenguajes = Menubutton(self.master, text='Menú lenguajes')

        mbn_lenguajes.menu = Menu(mbn_lenguajes)
        mbn_lenguajes['menu'] = mbn_lenguajes.menu

        var_javascript = IntVar()
        var_python = IntVar()
        var_java = IntVar()

        mbn_lenguajes.menu.add_command(label = 'JavaScript', command=self.mostrar_mensaje)
        mbn_lenguajes.menu.add_command(label = 'Python', command=self.mostrar_mensaje)
        mbn_lenguajes.menu.add_command(label = 'Java', command=self.mostrar_mensaje)

        mbn_lenguajes.pack()
    
    def mostrar_mensaje(self):
        messagebox.showinfo('Mensaje', 'Se ha hecho click en una opción de menú.')

def main():
    master = Tk()
    master.title('Lenguajes Programación')
    master.geometry('300x300')

    ventana = LenguajesProgramacion(master)

    master.mainloop()

if __name__ == '__main__':
    main()
