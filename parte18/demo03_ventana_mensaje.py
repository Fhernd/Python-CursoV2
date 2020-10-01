import tkinter as tk

ventana = tk.Tk()
ventana.geometry('300x300')

lbl_saludo = tk.Label(ventana, text='¡Hola, tk!', font=('Arial', 23), fg='green', bg='black', width=10)
lbl_saludo.pack()
lbl_saludo.place(x=20, y=150)

ventana.mainloop()
