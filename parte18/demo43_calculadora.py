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

        self.txt_expresion = Entry(frm_entrada, font=('Helvetica', 18, 'bold'), textvariable=self.entrada_expresion, width=50, bg='#EEE', bd=0, justify=RIGHT)
        self.txt_expresion.grid(row=0, column=0)
        self.txt_expresion.pack(ipady=10)

        frm_botones = Frame(self.master, width=312, height=273, bg='grey')
        frm_botones.pack()

        btn_limpiar = Button(frm_botones, text='C', fg='black', width=32, height=3, bd=0, bg='#EEE')
        btn_limpiar['cursor'] = 'hand2'
        btn_limpiar['command'] = self.limpiar
        btn_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        btn_dividir = Button(frm_botones, text='/', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_dividir['cursor'] = 'hand2'
        btn_dividir['command'] = lambda: self.presion_tecla('/')
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
        
        btn_cinco = Button(frm_botones, text='5', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_cinco['cursor'] = 'hand2'
        btn_cinco['command'] = lambda: self.presion_tecla(5)
        btn_cinco.grid(row=2, column=1, padx=1, pady=1)
        
        btn_seis = Button(frm_botones, text='6', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_seis['cursor'] = 'hand2'
        btn_seis['command'] = lambda: self.presion_tecla(6)
        btn_seis.grid(row=2, column=2, padx=1, pady=1)
        
        btn_resta = Button(frm_botones, text='-', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_resta['cursor'] = 'hand2'
        btn_resta['command'] = lambda: self.presion_tecla('-')
        btn_resta.grid(row=2, column=3, padx=1, pady=1)

        btn_uno = Button(frm_botones, text='1', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_uno['cursor'] = 'hand2'
        btn_uno['command'] = lambda: self.presion_tecla(1)
        btn_uno.grid(row=3, column=0, padx=1, pady=1)

        btn_dos = Button(frm_botones, text='2', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_dos['cursor'] = 'hand2'
        btn_dos['command'] = lambda: self.presion_tecla(2)
        btn_dos.grid(row=3, column=1, padx=1, pady=1)
        
        btn_nueve = Button(frm_botones, text='3', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_nueve['cursor'] = 'hand2'
        btn_nueve['command'] = lambda: self.presion_tecla(3)
        btn_nueve.grid(row=3, column=2, padx=1, pady=1)
        
        btn_suma = Button(frm_botones, text='+', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_suma['cursor'] = 'hand2'
        btn_suma['command'] = lambda: self.presion_tecla('+')
        btn_suma.grid(row=3, column=3, padx=1, pady=1)
        
        btn_cero = Button(frm_botones, text='0', fg='black', width=21, height=3, bd=0, bg='#EEE')
        btn_cero['cursor'] = 'hand2'
        btn_cero['command'] = lambda: self.presion_tecla(0)
        btn_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        
        btn_punto = Button(frm_botones, text='.', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_punto['cursor'] = 'hand2'
        btn_punto['command'] = lambda: self.presion_tecla('.')
        btn_punto.grid(row=4, column=2, padx=1, pady=1)
        
        btn_igual = Button(frm_botones, text='=', fg='black', width=10, height=3, bd=0, bg='#EEE')
        btn_igual['cursor'] = 'hand2'
        btn_igual['command'] = self.calcular
        btn_igual.grid(row=4, column=3, padx=1, pady=1)

    def limpiar(self):
        self.expresion = ''
        self.entrada_expresion.set('')

    def presion_tecla(self, tecla):
        self.expresion += str(tecla)
        self.entrada_expresion.set(self.expresion)

    def calcular(self):
        resultado = str(eval(self.expresion))
        self.entrada_expresion.set(resultado)
        self.expresion = ''

def main():
    app = Tk()
    ventana = CalculadoraApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()
