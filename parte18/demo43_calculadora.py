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

        btn_dividir = Button(frm_botones, text='/', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_dividir['cursor'] = 'hand2'
        btn_dividir['command'] = self.dividir
        btn_dividir.grid(row=0, column=3, padx=1, pady=1)

        btn_siete = Button(frm_botones, text='7', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_siete['cursor'] = 'hand2'
        btn_siete['command'] = lambda: self.presion_tecla(7)
        btn_siete.grid(row=1, column=0, padx=1, pady=1)
        
        btn_ocho = Button(frm_botones, text='8', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_ocho['cursor'] = 'hand2'
        btn_ocho['command'] = lambda: self.presion_tecla(8)
        btn_ocho.grid(row=1, column=1, padx=1, pady=1)
        
        btn_nueve = Button(frm_botones, text='9', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_nueve['cursor'] = 'hand2'
        btn_nueve['command'] = lambda: self.presion_tecla(9)
        btn_nueve.grid(row=1, column=2, padx=1, pady=1)
        
        btn_producto = Button(frm_botones, text='*', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_producto['cursor'] = 'hand2'
        btn_producto['command'] = lambda: self.presion_tecla('*')
        btn_producto.grid(row=1, column=3, padx=1, pady=1)
        
        btn_cuatro = Button(frm_botones, text='4', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_cuatro['cursor'] = 'hand2'
        btn_cuatro['command'] = lambda: self.presion_tecla(4)
        btn_cuatro.grid(row=2, column=0, padx=1, pady=1)
        
        btn_ocho = Button(frm_botones, text='5', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_ocho['cursor'] = 'hand2'
        btn_ocho['command'] = lambda: self.presion_tecla(5)
        btn_ocho.grid(row=2, column=1, padx=1, pady=1)
        
        btn_nueve = Button(frm_botones, text='6', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_nueve['cursor'] = 'hand2'
        btn_nueve['command'] = lambda: self.presion_tecla(6)
        btn_nueve.grid(row=2, column=2, padx=1, pady=1)
        
        btn_producto = Button(frm_botones, text='-', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_producto['cursor'] = 'hand2'
        btn_producto['command'] = lambda: self.presion_tecla('-')
        btn_producto.grid(row=2, column=3, padx=1, pady=1)

    def limpiar(self):
        pass
    
    def dividir(self):
        pass

    def presion_tecla(self, tecla):
        pass

def main():
    app = Tk()
    ventana = CalculadoraApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()
