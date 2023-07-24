from tkinter import *
from tkinter import ttk

class MDIWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("MDI Window")
        self.pack(fill=BOTH, expand=YES)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="New")
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

    def onExit(self):
        self.quit()


class FormWindow(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.title("Form Window")
        self.geometry("250x250")

        # Formulario
        Label(self, text="Código").pack()
        Entry(self).pack()
        Label(self, text="Nombre").pack()
        Entry(self).pack()
        Label(self, text="Precio").pack()
        Entry(self).pack()
        Label(self, text="Cantidad").pack()
        Entry(self).pack()
        Checkbutton(self, text="Disponible para venta").pack()
        Button(self, text="Crear").pack()


def main():
    root = Tk()
    root.geometry("600x400")

    mdi = MDIWindow(root)

    # Botón para abrir la ventana de formulario
    ttk.Button(mdi, text="Abrir formulario", command=lambda: FormWindow(mdi)).pack()

    root.mainloop()


if __name__ == '__main__':
    main()
