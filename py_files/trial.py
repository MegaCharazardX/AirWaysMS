# import tkinter as tk 
# root = tk.Tk()

# root.withdraw()
# scw = root.winfo_screenheight()
# sch = root.winfo_screenwidth()

# print(f"{scw}x{sch}")

# root.destroy()

from customtkinter import *

root = CTk()
# btns = []

# btn_data= {
#     1:"Start",
#     2:"Stop",
#     3:"Reset",
#     4:"Pause",
#     5:"Resume"
# }


# def on_btn_click(index):
#     print(f"{index} clicked. ")
    
# for id, label in btn_data.items() :
    
#     btn = CTkButton(root, text = label, command = lambda id=id: on_btn_click(id)).pack(pady = 10)
#     btns.append(btn)

def on_lbl_click(_label_txt):
    print(f"LABEL {_label_txt} Clicked")

lbl_text = [
            "Boston --------------- Thiruvananthapuram\n\n\n        25,000 rs",
            "label-2",
            "label-3"]
y_pos = 1
for txt in lbl_text :
    lbl = CTkLabel(root, text = txt, fg_color= "gray", width = 250, height=50)
    lbl.place(x = 0,y = y_pos)
    y_pos+=30
    lbl.bind("<Button-1>", lambda event, lbl_text = txt: on_lbl_click(lbl_text))
    lbl.bind("<Enter>", lambda event, lbl = lbl: lbl.configure(fg_color = "transparent"))
    lbl.bind("<Leave>", lambda event, lbl = lbl: lbl.configure(fg_color = "Gray"))

root.mainloop()




# CREATE TABLE user_acc (
#     'UID' int(100),
#     'UF_Name' varchar(100),
#     'UL_Name' varchar(100),
#     'U_Name' varchar(100),
#     'U_Pass' varchar(100),
#     'U_Phno' int(100),
#     'U_DOB' varchar(100),
#     'U_Age' int(4),
#     );