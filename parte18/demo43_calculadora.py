from tkinter import *

class CalculadoraApp:

    def __init__(self, master):
        self.master = master
        self.master.title('Calculadora App')
        self.master.geometry('312x324')
        self.master.resizable(0, 0)

        self.expresion = ''

        self.inicializar_gui()

    def inicializar_gui(self):
        self.entrada_expresion = StringVar()

        frm_entrada = Frame(self.master, width=312, height=50, bd=0, highlightbackground='black', highlightcolor='black', highlightthickness=2)
        frm_entrada.pack(side=TOP)

        txt_expresion = Entry(frm_entrada, font=('Helvetica', 18, 'bold'), textvariable=self.entrada_expresion, width=50, bg='#EEE', bd=0, justify=RIGHT)
        txt_expresion.grid(row=0, column=0)
        txt_expresion.pack(ipady=10)

        frm_botones = Frame(self.master, width=312, height=273, bg='grey')
        frm_botones.pack()

        btn_limpiar = Button(frm_botones, text='C', fg='black', width=32, height=3, bd=0, bg='#EEE')
        btn_limpiar['cursor'] = 'hand2'
        btn_limpiar['command'] = self.limpiar
        btn_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

    def limpiar(self):
        pass

def main():
    app = Tk()
    ventana = CalculadoraApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()
