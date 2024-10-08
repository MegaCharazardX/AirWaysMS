# import tkinter as tk 
# root = tk.Tk()

# root.withdraw()
# scw = root.winfo_screenheight()
# sch = root.winfo_screenwidth()

# print(f"{scw}x{sch}")

# root.destroy()

from customtkinter import *

root = CTk()
btns = []

btn_data= {
    1:"Start",
    2:"Stop",
    3:"Reset",
    4:"Pause",
    5:"Resume"
}


def on_btn_click(index):
    print(f"{index} clicked. ")
    
for id, label in btn_data.items() :
    
    btn = CTkButton(root, text = label, command = lambda id=id: on_btn_click(id)).pack(pady = 10)
    btns.append(btn)

root.mainloop()