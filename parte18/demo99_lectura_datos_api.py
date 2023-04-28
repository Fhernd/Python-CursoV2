import tkinter as tk
from tkinter import ttk

import requests


class LecturaDatosApi(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master

        self.inicializar_gui()
    
    