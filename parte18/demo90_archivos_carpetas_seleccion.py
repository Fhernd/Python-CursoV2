import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb


class Aplicacion(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Selector archivos y carpetas')
        self.geometry('350x350')

        btn_seleccionar_archivo = tk.Button(self, text='Seleccionar archivo...')
        btn_seleccionar_archivo['command'] = self.seleccionar_archivo
        
        btn_seleccionar_carpeta = tk.Button(self, text='Seleccionar carpeta...')
        btn_seleccionar_carpeta['command'] = self.seleccionar_carpeta

        btn_seleccionar_archivo.pack(padx=60, pady=10)
        btn_seleccionar_carpeta.pack(padx=60, pady=10)
    
    def seleccionar_archivo(self):
        tipos = (('Texto plano', '*.txt'), ('Imágenes', '*.jpg *.png *.gif'), ('Todos los archivos', '*'))

        archivo = fd.askopenfilename(title='Abrir archivo...', initialdir='/', filetypes=tipos)

        if archivo:
            mb.showinfo('Mensaje', archivo)
    
    def seleccionar_carpeta(self):
        directorio = fd.askdirectory(title='Abrir carpeta...', initialdir='/')

        if directorio:
            mb.showinfo('Mensaje', directorio)


def main():
    app = Aplicacion()
    app.mainloop()


if __name__ == '__main__':
    main()
