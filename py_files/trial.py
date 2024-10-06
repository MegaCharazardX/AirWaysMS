import tkinter as tk 
root = tk.Tk()

root.withdraw()
scw = root.winfo_screenheight()
sch = root.winfo_screenwidth()

print(f"{scw}x{sch}")

root.destroy()