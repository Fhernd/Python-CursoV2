import tkinter as tk

class PulsacionBotonesMouse():

    def __init__(self, master):
        self.master = master

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.master.bind('<Button-1>', self.click_principal)
        self.master.bind('<Button-2>', self.click_tercer_boton)
        self.master.bind('<Button-3>', self.click_secundario)
    
    def click_principal(self, evento):
        tk.Label(self.master, text='Botón principal').pack()
    
    def click_secundario(self, evento):
        tk.Label(self.master, text='Botón secundario').pack()
    
    def click_tercer_boton(self, evento):
        tk.Label(self.master, text='Tercer botón').pack()

def main():
    app = tk.Tk()
    app.title('Pulsación botones del mouse')
    app.geometry('400x700')

    ventana = PulsacionBotonesMouse(app)
    app.mainloop()

if __name__ == "__main__":
    main()
