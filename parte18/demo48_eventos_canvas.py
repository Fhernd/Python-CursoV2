from tkinter import messagebox, Canvas, Tk

class EventosCanvas:

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        canvas = Canvas(self.master, width=300, height=300)

        txt_click = canvas.create_text(130, 50, text='Click')
        txt_doble_click = canvas.create_text(130, 200, text='Doble click')

        canvas.tag_bind(txt_click, '<ButtonPress-1>', self.click)

        canvas.tag_bind(txt_doble_click, '<Double-1>', self.doble_click)

        canvas.pack()
    
    def click(self, evento):
        messagebox.showinfo('Mensaje', 'Se ha hecho click en un texto.')
    
    def doble_click(self, evento):
        messagebox.showinfo('Mensaje', 'Se ha hecho doble click en un texto.')

def main():
    master = Tk()
    master.title('Eventos Canvas')
    master.geometry('300x300')

    ventana = EventosCanvas(master)

    master.mainloop()

if __name__ == "__main__":
    main()
