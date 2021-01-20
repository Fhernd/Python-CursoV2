from tkinter import *

class CirculoEscalado(Frame):

    def __init__(self):
        Frame.__init__(self)
        
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Círculo - Escalado')
        self.master.geometry('220x280')

        self.sdr_escalado = Scale(self, from_=0, to=1000, orient=HORIZONTAL, command=self.escalar)
        self.sdr_escalado.pack(side=BOTTOM, fill=X)

        self.canvas = Canvas(self, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
    
    def escalar(self, valor):
        posicion = int(valor) + 10
        self.canvas.delete('circulo')
        self.canvas.create_oval(10, 10, posicion, posicion, fill='yellow', tags='circulo')

def main():
    CirculoEscalado().mainloop()

if __name__ == "__main__":
    main()
