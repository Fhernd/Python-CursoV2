from Tkinter import *

class CirculoEscalado(Frame):

    def __init__(self):
        Frame.__init__(self)
        
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Círculo - Escalado')
        self.master.geomtry('220x280')

        self.sdr_escalado = Scale(self, from_=0, to=200, orient=HORIZONTAL, command=self.escalar)
    
    def escalar(self, valor):
        pass

def main():
    CirculoEscalado().mainloop()

if __name__ == "__main__":
    main()
