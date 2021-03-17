import threading
import tkinter as tk
from tkinter import ttk
import requests

class DescargadorHtmlApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()

    def inicializar_gui(self):
        self.title('Descargador HTML')
        self.geometry('680x420')
        self.resizable(0, 0)

        self.frm_superior = tk.Frame(self)
        self.frm_superior.columnconfigure(0, weight=1)
        self.frm_superior.columnconfigure(1, weight=10)
        self.frm_superior.columnconfigure(2, weight=1)

        lbl_url = ttk.Label(self.frm_superior, text='URL:')
        lbl_url.grid(row=0, column=0, sticky=tk.W)
