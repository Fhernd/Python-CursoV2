import tkinter as tk
from urllib.request import urlopen


class DescargadorHTML(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.lbl_url = tk.Label(self, text='Dirección URL:')
        self.lbl_url.pack(side='top')

        self.txt_url = tk.Entry(self)
        self.txt_url.pack(side='top')

        self.btn_descargar = tk.Button(self, text='Descargar HTML', command=self.descargar_html)
        self.btn_descargar.pack(side='bottom')

        self.txa_contenido_html = tk.Text(self, height=20, width=20)
        self.txa_contenido_html.pack(side='bottom')
    
    def descargar_html(self):
        url = self.txt_url.get()
        
        html = urlopen(url).read().decode()
        self.txa_contenido_html.delete('1.0', 'end')
        self.txa_contenido_html.insert('end', html)


if __name__ == '__main__':
    root = tk.Tk()
    app = DescargadorHTML(master=root)
    app.mainloop()
