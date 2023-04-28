from tkinter import ttk 
import tkinter as tk 

ID = [1,2,3,4,5, 6, 7, 8, 9]
Names = ['Tom', 'Rob', 'Tim', 'Jim', 'Kim', 'Kim', 'Kim', 'Kim']
  
window = tk.Tk() 

treev = ttk.Treeview(window, selectmode ='browse') 
treev.pack(side='left',expand=True, fill='both') 
  

verscrlbar = ttk.Scrollbar(window,  
                           orient ="vertical",  
                           command = treev.yview) 
  
verscrlbar.pack(side ='right', fill ='y')   
treev.configure(yscrollcommand = verscrlbar.set) 

  
treev["columns"] = ('1', '2') 

treev['show'] = 'headings'
  
treev.column("1", width = 90, anchor ='c') 
treev.column("2", width = 90, anchor ='c') 


treev.heading("1", text ="ID") 
treev.heading("2", text ="Names") 
  
for x, y in zip(ID, Names):
    treev.insert("", 'end', values =(x, y)) 

window.mainloop() 