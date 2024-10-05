from customtkinter import *
from PIL import Image
import os 
from subprocess import call
import Global_Config as GC
import pymysql

m_r_width = 270
m_r_height = 450

root = CTk()
set_appearance_mode("Dark")
GC.centreScreen(root,root, m_r_width, m_r_height)
#---------globals--------
glb_clr_1 = "blue"
glb_clr_2 = "green"
glb_clr_3 = "yellow"
#---------------------FUNCTIONS---------------------------------



def createRadioButton (_frame ,_text : str , _value, _variable, _command,  _xpos : int, _ypos  : int):
    tmpRdBtn = CTkRadioButton(_frame, text = _text , value = _value, variable = _variable,width = 75, command = lambda :(_command()) )
    tmpRdBtn.place(x =_xpos, y = _ypos)
    return tmpRdBtn

#------------------------------------------------------
Main_fame = CTkFrame(root, width = m_r_width, height= m_r_height, border_width=2, border_color= glb_clr_1, fg_color="transparent")

# =>1-----Flight Booking---------

lbl = CTkLabel(Main_fame, text= "Book A Flight :- ", font = ("Freestyle Script", 18), bg_color="transparent", text_color= glb_clr_2)\
    .place(x = 10, y = 10)

book_a_fligt_radio_val = StringVar(value = "other")
rd_btn_y_pos = 40
return_radio_btn = createRadioButton(Main_fame,"Return","return_radio",book_a_fligt_radio_val,None,10, rd_btn_y_pos)#. place(x = 10, y = 25)
    
one_way_radio_btn = createRadioButton(Main_fame,"One Way", "oneway_radio", book_a_fligt_radio_val,None, 85, rd_btn_y_pos)#. place(x = 50, y = 25)
    
mulicity_radio_btn = createRadioButton(Main_fame, "Multicity", "multicity_radio", book_a_fligt_radio_val,None, 180, rd_btn_y_pos)#. place(x = 90, y = 25)

Origin_Airport = CTkComboBox(Main_fame,width=250, values=["From"]).place (x = 10, y = rd_btn_y_pos+30)
Dest_Airport = CTkComboBox(Main_fame,width=250, values=["To"]).place (x = 10, y = rd_btn_y_pos+59)
passenger_Class = CTkComboBox(Main_fame,width=250, values=["Passenger/Class"]).place (x = 10, y = rd_btn_y_pos+94)

#Date = CT
submit_btn = CTkButton(Main_fame, text = "Submit", width = 250, corner_radius=75).place(x = 10, y =185)
#----------------------------------------------------------------------------------
Main_fame.place(x = 0, y = 0)
root.resizable(True,True)
root.mainloop()