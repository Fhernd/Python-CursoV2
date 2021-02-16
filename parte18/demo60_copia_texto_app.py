import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class CopiaTextoApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.txa_origen = st.ScrolledText(self, width=50, height=10)
        self.txa_origen.grid(column=0, row=0, padx=10, pady=10)


def main():
    app = CopiaTextoApp()
    app.mainloop()

if __name__ == '__main__':
    main()
