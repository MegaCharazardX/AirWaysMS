from customtkinter import *
import tkinter as tk
root = CTk()
root.geometry("400x600")
set_appearance_mode("Dark")

appwidth = 350
appheight = 500
set_appearance_mode("dark")
root.geometry(f"{appwidth}x{appheight}")

glb_font_config = ("Arial" , 18, "bold" )
glb_btn_width = ((22/100)*int(appwidth))


#print((90/100)*int(appwidth))
app_frame = CTkFrame(root, width = appwidth, height = appheight,
                   border_width = 2, border_color = "blue", bg_color="transparent")

ans_frm_placeholder = tk.StringVar()
ans_frm_placeholder.set(0)

def ac():
    global _ans_frm_placeholder , ans_frm_placeholder
    _ans_frm_placeholder = "0"
    ans_frm_placeholder.set("0")

def _eval_():
    temp_ans = ans_frm_placeholder.get()
    if "x" in temp_ans:
        temp_ans = temp_ans.replace("x", "*")
        
    new_text = eval(temp_ans)
    
    ans_frm_placeholder.set(new_text)

def append(val):
    #new_text = ans_frm_placeholder.get() + val
    ans_frm_placeholder.set(val)
    
def onclick(val):
    global ans_frm_placeholder, _ans_frm_placeholder
    _ans_frm_placeholder = ans_frm_placeholder.get()
    #--VALIDATION--
    if _ans_frm_placeholder == "0" :
        if val not in "x-+/%" :
            ans_frm_placeholder.set("")
            _ans_frm_placeholder = ""
            append(val)
            
        else:            
            append(val)
    
    if ans_frm_placeholder.get() != "" :
        
        if _ans_frm_placeholder[-1] in "x-+/%" and val in "x-+/%" :
            pass
        
        else :
            new_text = _ans_frm_placeholder + val
            append(new_text)
    #--APPEND--
    #new_text = _ans_frm_placeholder + val

ans_frm = CTkFrame(root, width = appwidth, height = ((14/100)*int(appheight)),
                   border_width = 2, border_color = "black")
ans_frm.place(x = 0, y = 0)

ans_frm = CTkLabel(ans_frm, width = appwidth-2, height = ((14/100)*int(appheight)),
                   textvariable = ans_frm_placeholder, font= ("Arial" , 22, "bold" ), anchor="e")
ans_frm.place(x = 1, y = 0)

balance_frame_Height = appheight - (20/100)*int(appheight)
#print(balance_frame_Height)
# 
# # ACTIONS BTNS

equal_btn = CTkButton(root, width = glb_btn_width, height = ((40/100)*int(balance_frame_Height)), text="=",
                      font= glb_font_config,corner_radius= 30, command=lambda : (_eval_()))
equal_btn.place(x = 270, y = 330)

add_btn = CTkButton(root, width = glb_btn_width, height = ((20/100)*int(balance_frame_Height)), text="+",
                      font= glb_font_config,corner_radius= 30, fg_color= "#2e4760", command=lambda : (onclick("+")))
add_btn.place(x = 270, y = 245)

sub_btn = CTkButton(root, width = glb_btn_width, height = ((20/100)*int(balance_frame_Height)), text="-",
                      font= glb_font_config,corner_radius= 30, fg_color= "#2e4760", command=lambda : (onclick("-")))
sub_btn.place(x = 270, y = 160)

mul_btn = CTkButton(root, width = glb_btn_width, height = ((20/100)*int(balance_frame_Height)), text="x",
                      font= glb_font_config,corner_radius= 30, fg_color= "#2e4760", command=lambda : (onclick("x")))
mul_btn.place(x = 270, y = 75)

div_btn = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="/",
                      font= glb_font_config,corner_radius= 30, fg_color= "#2e4760", command=lambda : (onclick("/")))
div_btn.place(x = 185, y = 75)

backspace_btn = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="<",
                      font= glb_font_config,corner_radius= 30, fg_color= "#2e4760")
backspace_btn.place(x = 100, y = 75)

ac_btn = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="AC",
                      font= glb_font_config,corner_radius= 30, fg_color= "#2e4760", command=lambda : (ac()))
ac_btn.place(x = 5, y = 75)

mod_btn = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="%",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("%")))
mod_btn.place(x = 5, y = 417)

# NUMBER BTNS

btn_0 = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="0",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("0")))
btn_0.place(x = 100, y = 417)

btn_dot = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text=".",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick(".")))
btn_dot.place(x = 185, y = 417)

btn_1 = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text=" 1 ",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("1")))
btn_1.place(x = 5, y = 330)

btn_2 = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="2",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("2")))
btn_2.place(x = 100, y = 330)

btn_3 = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="3",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("3")))
btn_3.place(x = 185, y = 330) #--



btn_4 = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text=" 4 ",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("4")))
btn_4.place(x = 5, y = 245)

btn_5 = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="5",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("5")))
btn_5.place(x = 100, y = 245)

btn_6 = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="6",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("6")))
btn_6.place(x = 185, y = 245) #--



btn_7 = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text=" 7 ",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("7")))
btn_7.place(x = 5, y = 160)

btn_8 = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="8",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("8")))
btn_8.place(x = 100, y = 160)

btn_9 = CTkButton(root, width = glb_btn_width, height = ((18/100)*int(balance_frame_Height)), text="9",
                      font= glb_font_config,corner_radius= 30, fg_color= "#343638", command=lambda : (onclick("9")))
btn_9.place(x = 185, y = 160) #--


root.resizable(True,True)
root.mainloop()